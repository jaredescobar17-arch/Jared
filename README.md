# AI-Powered SEO Content Production — Research Corpus

A curated, source-grounded research corpus on **AI-powered SEO content production**:
using AI to plan, produce, and optimize content that wins in *both* classic search and
AI answer engines (AEO / GEO / LLMO). Built to support a real, future playbook — so the
emphasis is on **high-signal practitioners and primary-source material**, not volume.

> 10 carefully chosen experts · 9 full transcripts · 3 full-text long-form sources ·
> best-effort LinkedIn documentation for all 10 · collected 2026-06-19.

## Why this topic
AI search is splitting content strategy in two: ranking blue links *and* getting cited
inside ChatGPT/Perplexity/Google AI Mode. The people worth learning from are the ones
actually shipping AI-assisted content and measuring what happens — across strategy,
the mechanics AI rewards, and high-volume production.

## The 10 experts (and why them)
I optimized for **practitioners over commentators**, recent (2025–2026) on-topic output,
copyable workflows or original data, and platform diversity. Full rationale + links in
[`research/sources.md`](research/sources.md).

**Strategy & measurement**
1. **Kevin Indig** — Growth Memo; original, data-backed AI-search analyses.
2. **Ryan Law** — Director of Content @ Ahrefs; runs huge AEO studies *and* documents his exact AI writing process.
3. **Aleyda Solis** — Orainti; built the free AI Search Optimization Roadmap; vendor-neutral GEO/AEO voice.

**The AI-search mechanics content must satisfy**
4. **Mike King** — iPullRank; coined "Relevance Engineering," operationalized GEO/query fan-out.
5. **Bernard Huang** — Clearscope; hands-on AEO/GEO content workflows.
6. **Koray Tuğberk Gübür** — Holistic SEO; "Topical Authority" & Semantic SEO planning frameworks.

**High-volume production & automation**
7. **Jake Ward** — Byword founder; the most-cited public AI-content-at-scale case studies.
8. **Julian Goldie** — 300k-sub channel; end-to-end content/video/outreach automation.
9. **Nathan Gotch** — Gotch SEO; turns AI SEO/GEO into repeatable checklists.
10. **Gael Breton** — Authority Hacker; practical AI content/automation workflows (incl. Claude Code).

## What's in here
```
research/
├── sources.md                 # master list: 10 experts, links, dates, annotations
├── youtube-transcripts/       # 9 cleaned transcripts, organized by author
│   ├── aleyda-solis/  bernard-huang/  gael-breton/  julian-goldie/
│   ├── koray-gubur/   mike-king/      nathan-gotch/  ryan-law/
├── linkedin-posts/            # best-effort: one file per expert (profile + posts + summaries)
└── other/                     # full-text long-form sources
    ├── kevin-indig-growth-memo_the-alpha-is-not-llm-monitoring.md
    ├── ryan-law-ahrefs_my-complete-ai-content-process.md
    └── jake-ward_x-threads-digest.md
scripts/
└── extract_transcripts.py     # cleans raw caption HTML → tidy Markdown
```

## How content was collected
- **YouTube/podcast transcripts** — resolved each expert's recent on-topic video, pulled
  server-rendered captions (via `youtubetotranscript.com`, since YouTube's own domains are
  blocked from the build environment), then cleaned them with `scripts/extract_transcripts.py`.
  7 of 9 are near-verbatim; 2 (Julian Goldie, Aleyda Solis) are faithful condensations, flagged in-file.
- **Newsletters / blogs / X threads** — fetched full text where public (Substack, Ahrefs blog, Thread Reader).
- **LinkedIn** — **not scraped.** Anonymous fetches of public posts hit a login wall, so LinkedIn
  is documented best-effort (verified profile + specific post URLs + summaries). Verifiable full
  text for the LinkedIn-primary experts (Kevin Indig, Jake Ward) is captured from their open channels in `other/`.

## Honest limitations
- LinkedIn post *bodies* aren't reproduced (platform login wall) — URLs + summaries only.
- Two transcripts are condensed (clearly marked).
- Everything is dated and source-linked so it can be re-verified or refreshed.

## Suggested next step
Synthesize this corpus into a playbook with sections for: AI-search strategy & measurement,
content planning (topical authority), the AEO/GEO mechanics to satisfy, and production/automation
at scale — citing the specific transcripts and articles here.
