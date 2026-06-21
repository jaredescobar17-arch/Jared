#!/usr/bin/env python3
"""
extract_transcripts.py
----------------------
Cleans raw YouTube transcript HTML (fetched from youtubetotranscript.com, which
exposes YouTube's timed-text captions server-side) into plain-text Markdown files,
one per video, organized by author.

Pipeline used in this project:
  1. Resolve each expert's recent, on-topic video ID (via search / channel pages).
  2. Fetch https://youtubetotranscript.com/transcript?v=<VIDEO_ID> (server-rendered
     transcript; YouTube's own domains are not reachable from this sandbox).
  3. Run this script to strip site chrome and write /research/youtube-transcripts/.

Usage: python3 extract_transcripts.py
"""
import json, re, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "research", "youtube-transcripts")

def clean(raw: str) -> str:
    # Keep only the transcript body: from "## Transcript" to "Back To Top"
    start = raw.find("## Transcript")
    if start == -1:
        start = 0
    body = raw[start:]
    end = body.find("Back To Top")
    if end != -1:
        body = body[:end]
    # Drop the player toolbar that precedes the words ("...Translate")
    m = re.search(r"\nTranslate\n", body)
    if m:
        body = body[m.end():]
    # Remove markdown links / embeds / lone UI tokens
    lines = []
    for ln in body.splitlines():
        s = ln.strip()
        if not s:
            continue
        if s.startswith("[") and "](" in s:      # markdown links
            continue
        if s.startswith("http"):                  # bare urls / embeds
            continue
        if s in {"Pin video", "Transcript AI", "Copy", "Timestamp OFF",
                 "Translate", "## Transcript", "Transcript", "Get Free Transcript"}:
            continue
        lines.append(s)
    text = " ".join(lines)
    text = re.sub(r"\s+", " ", text).strip()
    # Soft-wrap into paragraphs every ~4 sentences for readability
    sents = re.split(r"(?<=[.!?]) +", text)
    paras, buf = [], []
    for i, snt in enumerate(sents, 1):
        buf.append(snt)
        if i % 4 == 0:
            paras.append(" ".join(buf)); buf = []
    if buf:
        paras.append(" ".join(buf))
    return "\n\n".join(paras)

def write(meta, text):
    d = os.path.join(OUT, meta["slug"])
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, meta["vid"] + ".md")
    header = (
        f"# {meta['title']}\n\n"
        f"- **Expert:** {meta['author']}\n"
        f"- **Channel / source:** {meta['channel']}\n"
        f"- **Video:** https://www.youtube.com/watch?v={meta['vid']}\n"
        f"- **Published:** {meta['date']}\n"
        f"- **Collected:** 2026-06-19 via youtubetotranscript.com (captions API)\n\n"
        f"---\n\n## Transcript\n\n"
    )
    with open(path, "w") as f:
        f.write(header + text + "\n")
    print(f"wrote {path}  ({len(text)} chars)")

# video_id -> (tool-result filename, metadata)
TR = "/sessions/nice-bold-volta/mnt/.claude/projects/C--Users-jared-AppData-Roaming-Claude-local-agent-mode-sessions-c4e45594-0548-48c4-b864-434a12fa5443-480f7779-6f3c-4bfa-b2ee-cbbe406f1983-local-2c451a69-29ce-4c6a-92de-3d818bdf7f27-outputs/dc9ff4d9-da14-473e-9dfa-220145494009/tool-results"

JOBS = [
 ("toolu_019275F5RFegVHEK2nt1Cmuu.json", {"vid":"blG6gss-mUY","slug":"gael-breton","author":"Gael Breton","channel":"Ahrefs Podcast (guest)","date":"2025","title":"Automate $10K/Month in Tasks with AI (REAL Workflows You Can Steal)"}),
 ("toolu_01Wbe3a4rtcoqGF28pJcawRM.json", {"vid":"ZytMamXMG0M","slug":"bernard-huang","author":"Bernard Huang","channel":"Clearscope","date":"2025","title":"How to Rank SEO Content in the Era of Generative AI"}),
 ("toolu_01TjfU1eub6eeggibTirc3ig.json", {"vid":"RMg2eTZL7Jk","slug":"bernard-huang","author":"Bernard Huang","channel":"Clearscope","date":"2026-02-13","title":"How To Do AEO (prompt research, query fan out, content): Live Session"}),
 ("toolu_01DYqvB87KwfzwGcHD85XBJt.json", {"vid":"0FmEV0jE5TQ","slug":"nathan-gotch","author":"Nathan Gotch","channel":"Nathan Gotch (Gotch SEO)","date":"2025","title":"AI SEO & GEO: The Ultimate Checklist for 2025"}),
 ("toolu_01PCD4dFHPSdWb8dwGPoc1aZ.json", {"vid":"5PAoIhyalsg","slug":"koray-gubur","author":"Koray Tuğberk Gübür","channel":"Interview","date":"2025","title":"Technical SEO & Semantic SEO with Koray Tugberk Gubur"}),
 ("toolu_01NrXhDQdrSrQcGwnb3eDeMb.json", {"vid":"pQLivtcqCZs","slug":"mike-king","author":"Mike King","channel":"The Page 2 Podcast","date":"2025","title":"Mike King on Relevance Engineering, AI Search & the Query Fan Out Technique"}),
 ("toolu_01DVeEkded737u1WH59HeArQ.json", {"vid":"mL1W1SMtTT4","slug":"ryan-law","author":"Ryan Law","channel":"Ahrefs Podcast","date":"2025","title":"How to Win in AI Search (Real Data, No Hype)"}),
]

for fn, meta in JOBS:
    p = os.path.join(TR, fn)
    raw = json.load(open(p))[0]["text"]
    write(meta, clean(raw))
