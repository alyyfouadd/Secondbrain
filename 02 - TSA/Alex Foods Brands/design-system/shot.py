import subprocess,os
BIN="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
HERE=os.path.dirname(os.path.abspath(__file__))
for n in [1,4,12,18]:
    css=f"<style>.page{{display:none!important}}.page:nth-of-type({n}){{display:block!important}}</style>"
    src=open(os.path.join(HERE,"ds.html"),encoding="utf-8").read().replace("</head>",css+"</head>",1)
    f=os.path.join(HERE,f"one{n}.html"); open(f,"w",encoding="utf-8").write(src)
    subprocess.run([BIN,"--headless","--disable-gpu","--no-sandbox","--virtual-time-budget=15000",
      f"--screenshot={os.path.join(HERE,f'page{n}.png')}","--window-size=794,1400","--hide-scrollbars",f],
      capture_output=True)
    print(n,"ok")
