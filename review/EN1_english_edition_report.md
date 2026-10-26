# EN1 — English edition report (2026-10-26)

Scope: English CH01–CH14, English workshop materials, instructor guide, glossary, site structure. Nothing was pushed or deployed.

## What exists
- `en/chapters/CH01.md` … `CH14.md` (internal status `Draft`, `last_reviewed` empty, no badge on the site, same as Korean).
- `en/workshop/`: `learner-workbook.md`, `sample-meeting-notes.md`, `sample-ai-output.md`, `workspace-template.md`, `instructor-guide.md` (Korean originals untouched in `workshop/`).
- `en/glossary.md`: Term | Korean | Definition / note (22 Korean rows translated + 8 added rows for Knowledge Base, Project Instructions, Source Material, Verification, Exception Handling, Version Management, Backup, Human Approval, each marked as added and pointing to the chapter that defines it).

## Checks that ran (structure only)
- `tools/content_audit.py --dist site/dist`: PASS 50 / FAIL 0, including the new ko/en parity check over 19 file pairs (headings, H3 count, code blocks and their line counts, table rows per table, checkboxes, `[S#]` references, URLs).
- Instructor guide: one intended extra table row (section 11 now also lists the English edition as a difference); the audit allows exactly +1 row for that file.
- Fictional values counted in ko and en workshop files are identical (KRW 12,500 / 11,800; 3,650 / 1,217 / 5.6%; 3,750 / 1,250 / 5.8%).
- Build: 48 pages; 0 broken internal links; language selector goes to the same page for every `/en/` page; separate Pagefind indexes for ko and en; instructor pages (both languages) are `noindex` and not in search; 375 px width shows no horizontal overflow.

## Not verified
- **Translation quality** is not machine-verifiable. Parity checks catch omissions and structure drift, not mistranslation or awkward phrasing. A human English review is still needed.
- Product names, menu labels, plan names and limits were taken over from the Korean chapters' official-source checks (S1–S15, checked 2026-10-26); they were not re-fetched in this phase.

## Judgment calls and open items
- The glossary entry for Work instructions still says "CH10 (planned)" because the Korean source says so; both should be updated together.
- Reading-guide wording in CH04 had a mandatory "[S6]" example removed so parity holds.
- Korean UI names are kept in quotes where the learner's own screen may be Korean (for example "Open with"), flagged in the text.
- The English overview SVG uses shortened chapter titles; the full titles are in the chapter pages and the sidebar.
- A bug found and fixed on the way: the return-to-portal banner showed Korean text on `/en/` pages because the locale prop is unset for the default locale; it now reads the URL.
- English start page title renders as "AI Workspace Handbook | AI Workspace Handbook" (cosmetic).

## Last steps to publish (not done)
1. Human English review of the chapters and workshop materials.
2. Push the handbook repo (also carries the unpushed L6 commits), confirm Pages build.
3. In the homepage repo, set the card's English link/availability, then Preview, then production only with approval.
