# Sources — AI-Powered SEO Content Production

**Topic:** AI-powered SEO content production (using AI to plan, produce, and optimize
content that ranks in both classic search and AI answer engines — AEO/GEO/LLMO).
**Collected:** 2026-06-19. **Curator:** Jared Escobar.

## How these 10 were chosen
Selection bar: **practitioners, not commentators.** Every person here actually ships
AI-assisted SEO content (or builds the tools/frameworks for it) and has *recent* (2025–2026),
on-topic output. I deliberately skipped generic "top SEO influencer" listicle names and
weighted for: (1) hands-on workflows you can copy, (2) original data or frameworks, and
(3) platform diversity (YouTube/podcast, newsletter, LinkedIn/X). The set spans the whole
production pipeline — strategy & measurement (Indig, Law, Solis), the AI-search mechanics
content must satisfy (King, Huang, Gübür), and high-volume production/automation
(Ward, Goldie, Gotch, Breton).

## How content was collected (methods)
- **YouTube/podcast transcripts:** resolved each expert's recent on-topic video ID, then
  pulled server-rendered captions via `youtubetotranscript.com` (YouTube's own domains are
  blocked from the build sandbox). Cleaned with `scripts/extract_transcripts.py`. → `youtube-transcripts/`
- **Newsletters / blogs / X threads:** fetched full text where publicly available
  (Substack, Ahrefs blog, Thread Reader). → `other/`
- **LinkedIn:** **not scraped.** Public post URLs return a login wall to anonymous clients,
  so LinkedIn is documented best-effort (profile + post URLs + summaries). → `linkedin-posts/`

| # | Expert | Primary surface | Verifiable full text collected |
|---|--------|-----------------|-------------------------------|
| 1 | Aleyda Solis | YouTube/podcast + newsletter | ✅ transcript |
| 2 | Kevin Indig | Newsletter (Growth Memo) | ✅ full newsletter |
| 3 | Ryan Law | Ahrefs blog + podcast | ✅ transcript + full article |
| 4 | Bernard Huang | YouTube webinars (Clearscope) | ✅ 2 transcripts |
| 5 | Mike King | Podcast/conference (iPullRank) | ✅ transcript |
| 6 | Gael Breton | Podcast/YouTube (Authority Hacker) | ✅ transcript |
| 7 | Julian Goldie | YouTube | ✅ transcript (condensed) |
| 8 | Nathan Gotch | YouTube (Gotch SEO) | ✅ transcript |
| 9 | Koray T. Gübür | YouTube/course (Holistic SEO) | ✅ transcript |
| 10 | Jake Ward | LinkedIn / X | ✅ X threads digest |

---

## 1. Aleyda Solis
**Who / why:** Founder of Orainti; creator of the free *AI Search Optimization Roadmap*
(LearningAISearch.com) and #SEOFOMO. One of the most rigorous, vendor-neutral voices on
GEO/AEO. Practitioner: consults brands and publishes a weekly video/news series.
- Profile: https://www.linkedin.com/in/aleyda · Site: https://www.aleydasolis.com/en/
- YouTube (Crawling Mondays): https://www.youtube.com/@CrawlingMondaysbyAleyda
- **In repo:** `youtube-transcripts/aleyda-solis/al-FuoXXQCs.md` — "The top SEO tip for 2026 of +12 SEO specialists" (2025-12-20); `linkedin-posts/aleyda-solis.md`

## 2. Kevin Indig
**Who / why:** Growth advisor (ex-Shopify, G2, Atlassian); Growth Memo (~23k subs) publishes
original, data-backed analyses of how AI search behaves differently from classic SEO.
Practitioner: runs experiments and advises growth teams.
- Profile: https://www.linkedin.com/in/kevinindig/ · Newsletter: https://www.growth-memo.com/
- **In repo:** `other/kevin-indig-growth-memo_the-alpha-is-not-llm-monitoring.md` (2025-11-26, full free text); `linkedin-posts/kevin-indig.md`

## 3. Ryan Law
**Who / why:** Director of Content Marketing at Ahrefs. Runs some of the largest AEO/AI-search
data studies *and* publicly documents his exact AI content production workflow. Gold for a playbook.
- Profile: https://uk.linkedin.com/in/thinkingslow · Site: https://ryanlaw.me/
- **In repo:** `youtube-transcripts/ryan-law/mL1W1SMtTT4.md` — "How to Win in AI Search (Real Data, No Hype)" (Ahrefs Podcast, 2025); `other/ryan-law-ahrefs_my-complete-ai-content-process.md` (2025-08-05, full article); `linkedin-posts/ryan-law.md`

## 4. Bernard Huang
**Who / why:** Co-founder of Clearscope. Runs hands-on webinars demonstrating real AEO/GEO
content workflows (prompt research, query fan-out, content scoring). Practitioner: builds the tooling.
- Profile: https://www.linkedin.com/in/bernardjhuang/ · Webinars: https://www.clearscope.io/webinars
- **In repo:** `youtube-transcripts/bernard-huang/ZytMamXMG0M.md` — "How to Rank SEO Content in the Era of Generative AI" (2025); `…/RMg2eTZL7Jk.md` — "How To Do AEO: Live Session" (2026-02-13); `linkedin-posts/bernard-huang.md`

## 5. Mike King
**Who / why:** Founder/CEO of iPullRank; coined "Relevance Engineering" and operationalized
Generative Engine Optimization; author of the *AI Search Manual*; 2025 Search Engine Land
Search Marketer of the Year. Deeply technical practitioner.
- Profile: https://www.linkedin.com/in/michaelkingphilly/ · AI Search Manual: https://ipullrank.com/ai-search-manual
- **In repo:** `youtube-transcripts/mike-king/pQLivtcqCZs.md` — "Mike King on Relevance Engineering, AI Search & the Query Fan Out Technique" (The Page 2 Podcast, 2025); `linkedin-posts/mike-king.md`

## 6. Gael Breton
**Who / why:** Co-founder of Authority Hacker. After the Helpful Content Update, pivoted to
teaching practical AI content/automation workflows (incl. automating with Claude Code).
Practitioner: builds and tests the automations he teaches.
- Profile: https://www.linkedin.com/in/gael-breton-78305118/ · Site: https://www.authorityhacker.com/
- **In repo:** `youtube-transcripts/gael-breton/blG6gss-mUY.md` — "Automate $10K/Month in Tasks with AI (REAL Workflows You Can Steal)" (Ahrefs Podcast, 2025); `linkedin-posts/gael-breton.md`

## 7. Julian Goldie
**Who / why:** Runs a 300k-sub YouTube channel that functions as a live feed of AI+SEO tactics;
ships end-to-end automation systems (content, video, outreach) with n8n/Make/AI. High-volume
production practitioner.
- YouTube: https://www.youtube.com/@JulianGoldieSEO · X: https://x.com/JulianGoldieSEO
- **In repo:** `youtube-transcripts/julian-goldie/HiivXpe2Slk.md` — "How to Automate SEO with AI in 2025" (condensed); `linkedin-posts/julian-goldie.md`

## 8. Nathan Gotch
**Who / why:** Founder of Gotch SEO Academy. Converts AI SEO/GEO into repeatable checklists
(e.g., a 97-point AI SEO & GEO checklist) and optimizes the same content for Google, ChatGPT,
and Perplexity. Practitioner-educator.
- YouTube: https://www.youtube.com/@nathangotch · Site: https://www.gotchseo.com/
- **In repo:** `youtube-transcripts/nathan-gotch/0FmEV0jE5TQ.md` — "AI SEO & GEO: The Ultimate Checklist for 2025"; `linkedin-posts/nathan-gotch.md`

## 9. Koray Tuğberk Gübür
**Who / why:** Founder of Holistic SEO & Digital; pioneered "Topical Authority" (Topical
Coverage + Historical Data) and Semantic SEO — the planning framework most AI-content teams
use for comprehensive, entity-driven content. Runs regular SEO A/B tests across Google/Bing/Yandex.
- Sites: https://www.holisticseo.digital/ · https://www.topicalauthority.digital/
- **In repo:** `youtube-transcripts/koray-gubur/5PAoIhyalsg.md` — "Technical SEO & Semantic SEO with Koray Tugberk Gubur"; `linkedin-posts/koray-gubur.md`

## 10. Jake Ward
**Who / why:** Founder of Byword (AI long-form content platform); ran an SEO agency doing
$20M+/yr for clients; publishes the most-cited public AI-content-*at-scale* case studies
(346 AI articles → ~123K traffic in 3 months; programmatic builds). Pure production practitioner.
- Profile: https://www.linkedin.com/in/jakezward · X threads: https://threadreaderapp.com/user/jakezward
- **In repo:** `other/jake-ward_x-threads-digest.md`; `linkedin-posts/jake-ward.md`

---

## Notes & limitations
- Two transcripts (Julian Goldie, Aleyda Solis) are stored as faithful **condensed** versions
  of the captions (flagged in their file headers); the other seven are near-verbatim cleaned captions.
- LinkedIn post *bodies* were not captured (login wall); URLs + summaries are provided instead,
  with full text sourced from each expert's open channels where possible.
- All links verified reachable at collection time (2026-06-19).
