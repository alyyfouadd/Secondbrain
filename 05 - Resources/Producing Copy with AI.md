---
status: active
project: meta
type: guide
---
# Producing Copy with AI

How [[TSA]] actually gets an AI to write in a brand's voice instead of producing the generic slop everyone else gets. Cross-client method, not tied to [[Alex Foods]], though that is the first job it runs on.

> **This never goes to a client.** Clause 5 of the [[Alex Foods]] scope, and the same clause in every TSA contract that follows: final deliverables are licensed to the client on full payment, **raw files, project files and TSA's working method stay agency property.** The brand voice guide is the client's. This note is how TSA operates, and it is the thing TSA actually sells.

---

## 1. The whole trick, in one line

**The voice guide is the prompt.**

Almost everyone asks an AI to "write a caption in our brand voice" and gets slop, then concludes AI cannot do voice. The model is not the problem. It was handed nothing and asked to invent a brand, so it averaged every brand it has ever read and gave back the mean. That is what slop is: the average of everything, which belongs to nobody.

A brand voice guide written properly — register, sentence length in actual numbers, words in and words out, who is being spoken to, real approved examples — **is not a document that describes the voice. It is the payload that produces it.** The same file does two jobs: it is a deliverable the client pays for, and it is the machine that makes the next three months of content.

That reframing is worth holding onto, because it changes what a voice guide should contain. A guide full of adjectives ("playful yet trustworthy") is useless to a person and useless to a model. A guide full of constraints is usable by both.

## 2. The four things loaded before a single word gets written

[[jareds-takes]] puts it as: context is king, feed it before it writes. Translated to a TSA client job, that means four files, every time, in this order.

1. **The craft rules.** [[Marketing]], and the playbook matching the task — [[marketing-copywriting]] for captions and headlines, [[marketing-content]] for calendars, [[marketing-fb-ads]] for paid.
2. **Who is being spoken to.** Not "our audience." The specific human, and critically **whether the person eating it and the person paying for it are the same person.** In FMCG they usually are not, and that single fact decides register.
3. **The voice.** That brand's tone block: register, sentence range, emoji cap, punctuation rule, words in, words out, and the never-say list.
4. **Approved examples.** Real captions that actually went out and were not rewritten.

Miss any of the four and the output degrades in a predictable way. Miss the craft rules and you get correct-sounding copy that sells nothing. Miss the audience and the register is wrong. Miss the voice and you get the average. Miss the examples and you get a competent imitation of a spec sheet.

## 3. The habit that compounds, and it costs nothing

**Keep a running approved-captions file per brand. Append every line that actually gets published.**

For the first batch the model is imitating a specification. After a month it is imitating real published work that a real person chose, which is a completely different quality of input. Nothing else in this method improves the output as much for as little effort, and almost nobody does it, because it feels like admin rather than work.

The rule: a caption goes in the file **only if it shipped unedited or near-unedited.** A file full of things you had to fix teaches the model to produce things you have to fix.

## 4. Volume, then the ear

Never ask for one caption. Ask for fifteen.

**The division of labour is fixed: the AI brings volume and structure, the human brings the ear.** That is the same split as the slogan method in [[Slogans and Song]], for the same reason. A model can generate forty options faster than a person can read them, and it cannot reliably tell which one a mother in Alexandria would actually say out loud. So it should never be asked to.

Never accept the first one. The first output is the model's average, and the average is exactly what you are trying to escape.

## 5. Arabic, specifically

This is where generic AI advice stops being enough.

- **Never write English and translate.** The output is always dead. Rhythm and wordplay do not survive the crossing, and a translated caption reads as a translated caption to every native speaker who sees it.
- **Watch for register drift.** An AI writing Arabic drifts toward فصحى, because that is what most written Arabic in its training is. Egyptian colloquial is spoken far more than it is written, so it is under-represented, and the model quietly formalises. Every batch gets checked for it.
- **Watch for the wrong dialect.** Gulf and Levantine phrasing turns up in Egyptian copy for the same reason. A native speaker catches it instantly, and a model will not catch it at all.
- **A native speaker signs off on every Arabic line.** Not a review of the strategy, a review of the sound. This is not a step to optimise away later.

## 6. The mechanical check nobody expects to need

**Run every batch against the never-say list before anything ships.**

This is not a nice-to-have, because **AI produces banned claims by default.** It is trained on a world of marketing copy that is full of "healthy," "100% natural," "boosts immunity," and it will reach for them unprompted on any food brief, cheerfully and confidently. On a food client that is a regulatory exposure, and on a paid campaign it is TSA's ad account carrying it.

So the never-say list is a filter applied to output, not just a rule stated in a brief. Mechanical, every batch, no exceptions.

## 7. What AI does not get to do

- **It never posts.** Drafts go to a human, always.
- **It never replies to a live comment autonomously.** The comment policy carries liability rules and a complaint script for a reason. An AI answering a contamination complaint on its own is a catastrophe with no upside.
- **It never invents a fact about the client.** Price, ingredients, availability, certifications. If it did not arrive from the client in writing, it does not exist, and a model asked a direct question will happily fill the gap.
- **It never decides what ships.** Selection is the human's job and it is most of the value.

## 8. When this becomes a Job note

[[jareds-takes]] describes a Jobs system: one folder per recurring job, with a same-named index note listing the steps and wiki-linking the files each step needs.

**This note is the method. A Job note would be the runbook**, and the vault's own trigger for building one is the second time a task gets explained from scratch. Monthly content production repeats three times on the [[Alex Foods]] contract alone, so it will earn one, and [[Active Priorities]] already carries the item. **Build it once month 1 has actually run**, so the runbook describes what happened rather than what was imagined.

---

**Related:** [[Marketing]] · [[jareds-takes]] · [[marketing-copywriting]] · [[TSA]] · [[Alex Foods]] · [[Brand Voice Guide]] · [[Slogans and Song]]
