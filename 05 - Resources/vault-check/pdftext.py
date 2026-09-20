# -*- coding: utf-8 -*-
"""Minimal PDF -> lines of text. No poppler, no third-party libraries.

Why this exists: the deliverable that actually reaches a client is the PDF,
and that is exactly where the BeBo reversal survived. check.py could read
every .md and .py in the vault and still pass while the shipped book said
the opposite on page 11.

Why it reconstructs LINES rather than dumping a blob of text: every other
check in vault-check is line-based, because a line is the unit that can
carry a history marker. A PDF is a bag of positioned glyphs, so the lines
have to be rebuilt from text-matrix y-positions before the same marker
rules can apply. Dump the whole page as one string and you are back to a
file-level check that can only pass everything or fail everything.

Handles what Chromium's HTML-to-PDF actually emits, which is what every
document in this vault is built with: FlateDecode content streams, Type0
and simple fonts, ToUnicode CMaps, and the Td/TD/Tm/T*/TJ/Tj/' operators.
Not a general PDF renderer.
"""
import re, zlib, collections, unicodedata

def _objects(data):
    """Map object number -> raw bytes, following the simple `N 0 obj` form."""
    out = {}
    for m in re.finditer(rb'(\d+)\s+(\d+)\s+obj\b', data):
        num = int(m.group(1))
        end = data.find(b'endobj', m.end())
        if end != -1:
            out[num] = data[m.end():end]
    return out

def _stream_bytes(obj):
    m = re.search(rb'stream\r?\n', obj)
    if not m:
        return None
    raw = obj[m.end():]
    e = raw.rfind(b'endstream')
    if e != -1:
        raw = raw[:e]
    if b'/FlateDecode' in obj:
        try:
            return zlib.decompress(raw.rstrip(b'\r\n'))
        except zlib.error:
            for trim in (0, 1, 2):
                try:
                    return zlib.decompressobj().decompress(raw[trim:])
                except zlib.error:
                    continue
            return None
    return raw

def _tounicode(stream):
    """Parse a ToUnicode CMap into {code: text}."""
    cmap = {}
    if not stream:
        return cmap
    txt = stream.decode('latin-1', 'replace')
    for blk in re.findall(r'beginbfchar(.*?)endbfchar', txt, re.S):
        for src, dst in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', blk):
            cmap[int(src, 16)] = _utf16(dst)
    for blk in re.findall(r'beginbfrange(.*?)endbfrange', txt, re.S):
        for lo, hi, dst in re.findall(
                r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', blk):
            lo, hi = int(lo, 16), int(hi, 16)
            base = int(dst, 16)
            for i in range(hi - lo + 1):
                cmap[lo + i] = chr(base + i) if base >= 32 else ''
    return cmap

def _utf16(hexstr):
    b = bytes.fromhex(hexstr)
    if len(b) >= 2:
        try:
            return b.decode('utf-16-be', 'replace')
        except Exception:
            pass
    return b.decode('latin-1', 'replace')

def _fonts(objs, page_obj):
    """code-map per font resource name, e.g. {'/F1': {code: char}}"""
    fonts = {}
    res = re.search(rb'/Font\s*<<(.*?)>>', page_obj, re.S)
    names = {}
    if res:
        for n, ref in re.findall(rb'(/\w+)\s+(\d+)\s+0\s+R', res.group(1)):
            names[n.decode()] = int(ref)
    for name, num in names.items():
        fo = objs.get(num, b'')
        tu = re.search(rb'/ToUnicode\s+(\d+)\s+0\s+R', fo)
        if tu:
            fonts[name] = _tounicode(_stream_bytes(objs.get(int(tu.group(1)), b'')))
        else:
            desc = re.search(rb'/DescendantFonts\s*\[\s*(\d+)\s+0\s+R', fo)
            fonts[name] = {}
    return fonts

_NUM = r'[-+]?[\d.]+'

# One named group per operator. A single hand-built alternation with numbered
# groups was the first attempt and the indices silently misaligned, which
# extracted zero lines while looking perfectly reasonable.
_OPS = re.compile(r"""
    (?P<tf>/(?P<font>\w+)\s+[\d.]+\s+Tf)
  | (?P<bt>\bBT\b)
  | (?P<td>(?P<tdx>%(n)s)\s+(?P<tdy>%(n)s)\s+Td\b)
  | (?P<tdd>(?P<tddx>%(n)s)\s+(?P<tddy>%(n)s)\s+TD\b)
  | (?P<tm>%(n)s\s+%(n)s\s+%(n)s\s+(?P<tmd>%(n)s)\s+(?P<tmx>%(n)s)\s+(?P<tmy>%(n)s)\s+Tm\b)
  | (?P<tl>(?P<tlv>%(n)s)\s+TL\b)
  | (?P<tstar>T\*)
  | (?P<tj>\[(?P<tjbody>.*?)\]\s*TJ)
  | (?P<sj>\((?P<sjbody>(?:\\.|[^\\()])*)\)\s*Tj)
  | (?P<hj><(?P<hjbody>[0-9A-Fa-f\s]+)>\s*Tj)
""" % {'n': _NUM}, re.X | re.S)

def page_lines(objs, page_obj, content):
    """Rebuild visual lines from a page's content stream.

    Glyphs are grouped by their text-matrix y-position, then ordered by x.
    That grouping is the whole point: it turns a bag of positioned glyphs
    back into lines, which is the unit a history marker can sit on.
    """
    fonts = _fonts(objs, page_obj)
    txt = content.decode('latin-1', 'replace')
    rows = collections.defaultdict(list)
    cur = {}
    x = y = leading = 0.0
    flip = False
    for m in _OPS.finditer(txt):
        k = m.lastgroup
        if m.group('tf'):
            cur = fonts.get('/' + m.group('font'), {})
        elif m.group('bt'):
            x = y = 0.0
        elif m.group('td'):
            x += float(m.group('tdx')); y += float(m.group('tdy'))
        elif m.group('tdd'):
            leading = -float(m.group('tddy'))
            x += float(m.group('tddx')); y += float(m.group('tddy'))
        elif m.group('tm'):
            x = float(m.group('tmx')); y = float(m.group('tmy'))
            # Chromium writes `1 0 0 -1 x y Tm`: d is negative, so the text
            # space is y-down and the page reads in ASCENDING y, not descending.
            flip = float(m.group('tmd')) < 0
        elif m.group('tl'):
            leading = float(m.group('tlv'))
        elif m.group('tstar'):
            y -= leading
        elif m.group('tj'):
            rows[round(y, 1)].append((x, _decode_tj(m.group('tjbody'), cur)))
        elif m.group('sj'):
            rows[round(y, 1)].append((x, _decode_str(m.group('sjbody'), cur)))
        elif m.group('hj'):
            rows[round(y, 1)].append((x, _decode_hex(m.group('hjbody'), cur)))
    out = []
    for yy in sorted(rows, reverse=not flip):
        line = ''.join(t for _, t in sorted(rows[yy], key=lambda q: q[0])).strip()
        if line:
            out.append(line)
    return out

def _decode_str(s, cmap):
    b = s.encode('latin-1', 'replace').decode('unicode_escape').encode('latin-1', 'replace')
    if cmap:
        return ''.join(cmap.get((b[i] << 8) | b[i + 1], '') for i in range(0, len(b) - 1, 2))
    return b.decode('latin-1', 'replace')

def _decode_hex(h, cmap):
    h = re.sub(r'\s', '', h)
    if cmap:
        return ''.join(cmap.get(int(h[i:i + 4], 16), '') for i in range(0, len(h) - 3, 4))
    return bytes.fromhex(h).decode('latin-1', 'replace')

def _decode_tj(body, cmap):
    parts = []
    for m in re.finditer(r'\((.*?)(?<!\\)\)|<([0-9A-Fa-f\s]+)>', body, re.S):
        if m.group(1) is not None:
            parts.append(_decode_str(m.group(1), cmap))
        else:
            h = re.sub(r'\s', '', m.group(2))
            parts.append(''.join(
                cmap.get(int(h[i:i + 4], 16), '') for i in range(0, len(h) - 3, 4)
            ) if cmap else '')
    return ''.join(parts)

def pages(path):
    """[(page_number, [line, ...]), ...] in document order."""
    data = open(path, 'rb').read()
    objs = _objects(data)
    out = []
    for num, obj in sorted(objs.items()):
        if b'/Type' not in obj or b'/Page' not in obj or b'/Pages' in obj:
            continue
        refs = re.search(rb'/Contents\s+(?:(\d+)\s+0\s+R|\[(.*?)\])', obj, re.S)
        if not refs:
            continue
        nums = ([int(refs.group(1))] if refs.group(1)
                else [int(x) for x in re.findall(rb'(\d+)\s+0\s+R', refs.group(2))])
        content = b''.join(_stream_bytes(objs.get(n, b'')) or b'' for n in nums)
        out.append((len(out) + 1, page_lines(objs, obj, content) if content else []))
    return out

def variants(line):
    """Every form a line might have to be matched in.

    Arabic comes out of a PDF in VISUAL order as presentation-form glyphs, so
    a pattern written the way a human types it ("ظرف بودرة") never matches the
    raw extraction. NFKC folds the presentation forms back to base letters and
    reversing restores logical order. Latin is unaffected by either, so all
    three forms are offered and the caller matches against any of them.
    """
    n = unicodedata.normalize('NFKC', line)
    return (line, n, unicodedata.normalize('NFKC', line[::-1]))

def lines(path):
    """Every text line in the document, flat, in reading order."""
    return [ln for _, ls in pages(path) for ln in ls]
