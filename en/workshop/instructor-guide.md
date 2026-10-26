# Instructor guide (instructor-guide)

> **This is the instructor guide. It contains answers and error explanations, so learners should open it after they finish the exercises.** This document is public material (the website separates it from the exercise materials and menu, and excludes it from search), but it is not handed out to workshop participants during the exercises. The answers and error explanations for the fictional AI outputs are in section 7. The participant materials are four files: `sample-meeting-notes.md`, `sample-ai-output.md`, `learner-workbook.md`, and `workspace-template.md` (the English files in en/workshop/).
>
> This is an operating guide built by connecting CH01 to CH14 with `review/WORKSHOP_6H_PLAN.md`; it does not create new teaching content. **Every time allocation in this guide is an unverified estimate.** The workshop has never been run with real learners. Do not assume the timing works until after the pilot (P5 in `review/INTEGRATED_REVIEW_PLAN.md`).

## 1. Purpose and principles

- **Purpose:** Each participant carries one candidate task A from CH01 through CH14 and builds a *draft design of an AI workspace*.
- **Workshop completion ≠ work environment completion.** What the 6 hours aim for is a *Level 1 draft of candidate A* (sections 2-3). Finishing the design and reaching Levels 2 and 3 are follow-up assignments, and that judgment is the participant's self-assessment. Attending the workshop and filling in part of the forms is not enough to mark any level as "achieved."
- **Use fictional data only.** No real customer information, personal information, company confidential information, passwords, or API keys are entered into an AI service in any exercise. The same applies to the instructor's demonstrations.
- **An AI service is not required.** Even if a participant has no account or the organization's policy does not allow it, every required exercise can be done with the fictional AI outputs and design sheets (section 8).
- **Do not claim effects.** Say that "it saves time" and "it reduces errors" are not things this book has confirmed.

## 2. Material package

| File | For | Use | Contains answers |
|---|---|---|---|
| `en/workshop/sample-meeting-notes.md` | Participants | Six fictional meeting materials (Material 1 to 6) | No |
| `en/workshop/sample-ai-output.md` | Participants | Three fictional AI outputs (A, B, C) | No |
| `en/workshop/learner-workbook.md` | Participants | A record document collecting the core exercise forms from CH01 to CH14 | No |
| `en/workshop/workspace-template.md` | Participants | Form for the workspace map and rule set (CH14 [2][3]) | No |
| `en/workshop/instructor-guide.md` | Instructor (public material; best opened after the exercises) | Running order, operating plans, answers and explanations, questions, alternative paths, Level criteria | **Yes (section 7)** |
| Textbook chapters `en/chapters/CH01 to CH14.md` | Reference | Concept explanations and the original forms | Some chapters (CH03, CH06, CH09, CH12) contain the author's commentary in the text; see section 12 |

(The Korean files are under `workshop/` and `ko/chapters/`.)

## 3. The state the workshop aims for, and follow-up assignments

| When | Expected state | Label |
|---|---|---|
| Right after the workshop | Candidate A's workspace map, material review, folder and storage rules, project design, knowledge documents and index, request and fact check, work instructions v01, flowchart and human approval points, draft verification and backup plans, connection check | `Level 1 in progress (candidate A draft)` |
| After the follow-up assignment | All 8 documents exist, the connection check sheet is consistent, and the work can be explained from the documents alone | Level 1 achieved (self-assessment) |
| Later | Local folders, setup in available tools, backup and restore of fictional files, passing the pre-run check | Level 2 |
| Later | Real AI work done, verified, and backed up with approved work data | Level 3 |

*We have not tested whether every participant can finish all Level 1 documents within 6 hours.*

## 4. Preparation

### 4-1. Facilitator preparation (before the workshop)

- [ ] Prepare the four participant materials as printouts or files (keep this guide, which contains the answers, separately).
- [ ] Re-check the official sources S1 to S15 the day before (many documents show only relative dates). Check the Korean-language screen menu names.
- [ ] Ask the person in charge which AI services, cloud services, and backup locations your organization allows.
- [ ] Prepare only fictional data in the demonstration environment. Make sure no real work conversations are visible in the demo account.
- [ ] Venue: provide desks, and make sure participants can write on printouts or open the documents on a laptop. The required exercises can be done without internet.

### 4-2. Pre-work for participants (estimated about 60 minutes, unverified)

Pre-work 1 to 4 in `learner-workbook.md`: a list of last week's tasks with a candidate check, a 5-question work environment diagnosis, a service check table (including whether the organization allows it), a practice folder and 8 fictional files. Participants who skip the pre-work will run short of time on site, so have them use fictional examples in the CH01 and CH04 blocks and mark them `[Fictional example]`.

## 5. Six-hour plan (one session)

360 minutes = 320 minutes of class + 40 minutes of breaks. **Demonstration (instructor)** and **exercise (participants)** are shown separately. All times are unverified estimates, and the only cells to fill in are the *part of the core forms* listed below. Do not change the order of the chapters. At the start of each block, say "what from the previous chapter this chapter uses," and at the end say "the next chapter uses this output."

| Time | Minutes (demo + exercise) | Block / chapter | Demonstration (instructor) | Participant exercise (workbook) | Check points |
|---|---|---|---|---|---|
| 0:00 | 20 (6+14) | 1 / CH01 | Introduce the three concepts (workspace, workflow, harness), example of writing the candidate A card (organizing meeting minutes) | Block 1 candidate A card | Is the purpose written in one line? Is the candidate not too big? |
| 0:20 | 20 (6+14) | 2 / CH02 | The five boxes and the idea of a copy, example of a movement path | Block 2 [0][1], 3 to 4 movement path rows, one workspace map | Tell them box ④ can start as a single folder. "Don't know" is also an answer |
| 0:40 | 30 (10+20) | 3 / CH03 | Difference between transmission, retention, and training use; A/B/C tiers (not a legal classification, the organization's rules come first); masking example | Block 3 Exercise 1 (classification), Exercise 2 (mask Material 1), Exercise 3 (review the candidate A material) | **Make sure no real personal information is used here.** If judgments differ on items 2 and 3, choose the more conservative tier |
| 1:10 | 15 (4+11) | 4 / CH04 | Showing file extensions, folder structure, file naming rule | Block 4 [1][2][3] | Add new folders only; do not move or delete existing files |
| 1:25 | 15 (4+11) | 5 / CH05 | Sync ≠ backup (official basis S11, S14, S13), least privilege | Block 5 [1][2][4] (design only) | Do not have them actually upload or share. Is the backup cell not empty? |
| 1:40 | 20 | Break | | | |
| 2:00 | 35 (10+25) | 6 / CH06 or CH07 | Project concept and where instructions go (one service only), demo with fictional data, name and description vs instructions (Claude) | Block 6 [1] to [5]. If no account: [4] design sheet + fictional AI draft A for [5] | Make sure sharing and external connections are not turned on. Are the rules in the instructions? Run-type label |
| 2:35 | 20 (6+14) | 7 / CH08 | Knowledge vs work files, the four types, K01 example | Block 7 K01 document (based on Material 5), [3] index | Are the source and update date written? |
| 2:55 | 35 (10+25) | 8 / CH09 | Six parts of a work request, fact / inference / assumption / unconfirmed, recalculation demo (fictional) | Block 8 [1][2][3][4], fictional AI draft B | **Do not tell them the answers first.** Have them find each sentence in the source text |
| 3:30 | 20 | Break (meal) | | | |
| 3:50 | 35 (10+25) | 9 / CH10 | Prompt vs work instructions, 8 elements, the public harness case is only about *the idea of splitting documents* | Block 9 [1] work instructions v01, [2] tests T1 and T2 | Are there things it does not do and exception handling? Did they find vague sentences? |
| 4:25 | 25 (7+18) | 10 / CH11 | Example of an input → processing → verification → output flowchart, criteria for human approval points | Block 10 [1] flowchart, [3] approval points, [4] at least 3 exceptions | Is there an approval point before sharing or sending? |
| 4:50 | 25 (7+18) | 11 / CH12 | Two-way comparison, error types, criteria for deciding to re-run | Block 11 [1] checklist, [2] error log (fictional AI draft C), [4] final confirmation | Do not say how many. Did they also do the source text → result direction? |
| 5:15 | 15 (4+11) | 12 / CH13 | Sync propagating deletions, Recycle Bin / trash period (S14, S13), version in the file name | Block 12 [1] backup plan, [4] recovery checklist | Is the backup location one that does not sync, and did they check the organization's rules? |
| 5:30 | 30 (8+22) | 13 / CH14 | Connection check sheet, run-type label, Level 1 to 3 | Block 13 [1] connection check, `workspace-template.md` A, [4] pre-run check, [7] judgment | **Label the Level honestly.** Section 9 |
| 6:00 | | End | Explain the follow-up assignment (end of `learner-workbook.md`) | | |

**What to keep in mind when demonstrating:** Use fictional data only. If you demonstrate a real AI service, say aloud that the screen is `[Live AI run: fictional data]`. AI responses can differ each time, so *do not promise that the demo will produce the same errors as the fictional AI draft.* If the demo result differs from what you expected, show it as it is and apply the verification procedure.

## 6. Two 3-hour sessions

Each session is 180 minutes. All times are unverified estimates, and a follow-up assignment sits between the sessions.

### 6-1. Session 1 (180 minutes): foundations and environment

| Time | Minutes (demo + exercise) | Content |
|---|---|---|
| 0:00 | 5 | Start card (choose a path), explain the workshop goal (Level 1 draft) and run-type labels |
| 0:05 | 20 (6+14) | CH01 candidate A card |
| 0:25 | 20 (6+14) | CH02 workspace map |
| 0:45 | 30 (10+20) | CH03 information tiers, masking, candidate A material review |
| 1:15 | 15 (4+11) | CH04 folders, file names, material list |
| 1:30 | 15 (4+11) | CH05 cloud storage and sharing design |
| 1:45 | 10 | Break |
| 1:55 | 35 (10+25) | CH06 or CH07 Project (one service) |
| 2:30 | 20 (6+14) | CH08 knowledge documents and index |
| 2:50 | 10 | Wrap-up, explain the **assignment before session 2** |

**Assignment between sessions 1 and 2 (estimated about 60 to 90 minutes, unverified):** Fill in the empty cells in blocks 1 to 8, and finish the knowledge folder, K01, the index, and the source log. If your account allows it, try uploading fictional data to the Project (after confirming the organization allows it). Bring `learner-workbook.md` to session 2.

### 6-2. Session 2 (180 minutes): use, verification, completion

| Time | Minutes (demo + exercise) | Content |
|---|---|---|
| 0:00 | 5 | Check the previous session's outputs (those who have none continue with fictional examples) |
| 0:05 | 35 (10+25) | CH09 work request, fact-check table, numeric verification |
| 0:40 | 35 (10+25) | CH10 work instructions v01, tests T1 and T2 |
| 1:15 | 10 | Break |
| 1:25 | 25 (7+18) | CH11 flowchart, approval points, exceptions |
| 1:50 | 25 (7+18) | CH12 verification checklist, error log |
| 2:15 | 15 (4+11) | CH13 backup plan, recovery checklist |
| 2:30 | 30 (8+22) | CH14 connection check, pre-run check, level judgment |

**Follow-up assignment after session 2:** the follow-up assignment table at the end of `learner-workbook.md`.

### 6-3. Cautions when splitting into two sessions

- Participants who attend only session 1 may just read CH09 to CH14 as `[Fictional example]`, but in that case their level cannot go beyond Level 1.
- For participants who first come to session 2, have them fill in CH01 to CH08 using the fictional setting in `sample-meeting-notes.md` and mark every cell `[Fictional example]`.

## 7. Instructor answers and error explanations (open after the exercises)

> The following is *the author's criteria, not an answer key*. If a participant makes a different reasonable judgment, ask for the reasoning. Do not tell them the answers first; compare after participants have filled in the tables.

### 7-1. CH03 Exercise 1: classifying the 12 fictional files

| No. | Author's tier | Reason |
|---|---|---|
| 1 | A | Already public |
| 2 | B | Internal information. Masking names and amounts leaves only the structure. Only in an allowed service |
| 3 | B | Trade terms are internal information. If it is still sensitive after masking the client and amounts, it can be changed to C |
| 4 | C | Personal information with names and contact details tied together |
| 5 | C | Pay by individual is personal information and must be handled as sensitive |
| 6 | C | Contains a password |
| 7 | C | Contains an API key |
| 8 | A | Already public |
| 9 | C | Likely to be covered by contractual confidentiality. Check the contract |
| 10 | C | Material before release to investors. Needs your organization's approval |
| 11 | C | Health information is generally treated as sensitive |
| 12 | A | A form with no content |

Items 2 and 3 can be a judgment call between B and C. If a participant cannot decide, have them choose the more conservative tier and ask the person in charge. These tiers are the author's teaching criteria, not a legal classification.

### 7-2. CH03 Exercise 2: masked example (Material 1)

```text
Sales meeting notes, Month ○, 2026 (masked version)
Attendees: Manager A, Associate B, Staff C
Agenda 1) Lowering the per-unit price of parts delivered to Client X
 - Manager A opposed the cut. Associate B will send a revised proposal to the Client X contact by next week
Agenda 2) Adjusting Staff C's vacation schedule
 - Staff C requested vacation in November
```

No names, amounts, or contact details may remain. Even after masking, people inside the company may be able to guess who is meant, so have participants check that the organization allows its use before using it. *The differences between Material 1 and Material 2 are recorded in section 11.*

### 7-3. Fictional AI draft A (CH06 section 6): 5 errors

Source text: Material 2.

| No. | Draft | Source text | Type |
|---|---|---|---|
| 1 | "Decided to send a reduction proposal to Client X" | Will send a revised proposal | Distortion |
| 2 | "By next Tuesday" | "By next week"; no day of the week is set | Assumption (a weekday that is not there) |
| 3 | "Approved Staff C's November vacation", owner "Manager A" | Vacation was requested. The notes have no approval decision and no owner | Fabrication |
| 4 | "Wednesday of the fourth week of October" | The date is undecided | Fabrication |
| 5 | "Open items: None" | The substitute worker and the meeting date are still undecided | Omission |

### 7-4. Fictional AI draft B (CH09 section 6): 6 errors + 3 calculations + 1 quotation

Source text: Material 2 and the quantity table.

| No. | Problem | Correct content | Type |
|---|---|---|---|
| 1 | "Decided to send a price-cut proposal" | Will send a revised proposal | Distortion |
| 2 | Quotation in quotation marks: "A price cut is absolutely out of the question" | The notes say "opposed the cut". The quoted words are not in the notes | Fabrication (quotation) |
| 3 | "Next Tuesday" | "By next week" | Assumption |
| 4 | "Approved the vacation and named Associate B as the substitute worker" | Applied for vacation. The substitute worker was not decided | Fabrication |
| 5 | "Held on Wednesday" | Fourth week of October, date undecided | Fabrication |
| 6 | "Open items: None" | Substitute worker undecided, meeting date undecided | Omission |

| Calculation | Draft | Correct value (formula) |
|---|---|---|
| Total, July to September | 3,750 units | **3,650 units** (1,200 + 1,350 + 1,100) |
| Monthly average | 1,250 units | **About 1,217 units** (3,650 ÷ 3) |
| Cut rate | 5.8% | **5.6%** (700 ÷ 12,500 = 0.056) |

**Expected answer for the CH09 [2] fact-check table (Nos. 1 to 6):** The verdict in every row is "wrong." The category column has sentences written as if they were fact but with no basis in the source text or that differ from it, so you can explain No. 1 as distortion, No. 2 as fabrication, No. 3 as assumption, No. 4 as fabrication, No. 5 as fabrication/assumption, and No. 6 as omission (not matching the facts). If participants write only "fact/inference/assumption/unconfirmed" in the category cell, it can be confusing because these are "wrong sentences written like facts," so explain the category cell as *whether the content is in the source text (fact) / written without being in the source text (inference or assumption)* and gather the verdicts as wrong. (This follows the category criteria in section 2-5 of CH09.)

**What the corrected version should look like:** Agenda 1 has Manager A's opposition and Associate B's delivery of the revised proposal ("by next week"); agenda 2 has Staff C's November vacation request and the substitute worker undecided; agenda 3 has the fourth week of October, date undecided; open items have the undecided substitute worker and meeting date; and a "Needs confirmation" list is included. The numbers are 3,650 / about 1,217 / 5.6%.

### 7-5. Fictional AI draft C (CH12 section 6): 8 items

Source text: Material 3. The only document in the index is K01.

| No. | Error | Type / severity | Correct content / action |
|---|---|---|---|
| 1 | "By October 31" | Date / high | October 30 |
| 2 | "Staff C will review it personally" | Person / high | Written by Staff C, reviewed by Associate B |
| 3 | "Wednesday of the third week of November" | Fabrication, distortion / high | One day in the second week of November, date undecided |
| 4 | "Associate B is in charge" | Fabrication / high | Owner needs confirmation |
| 5 | "Due to a logistics problem" | Fabrication / high | Reason not yet confirmed |
| 6 | "(According to rule K02)" | Source / medium | Delete K02 (or correct it to K01) |
| 7 | Omission: the deadline by which Manager A will reply by phone on October 25 | Omission / medium | Add "Manager A, phone, October 25" |
| 8 | Format: paragraphs instead of a table, no "Needs confirmation" list | Format / low | A table and a list of items needing confirmation, per the work instructions format |

**Expected answer for the judgment table:** There are 4 high-severity errors and several fabrications, so *discard, find the cause, and re-run* (add "do not make up dates, weekdays, or owners" and "only document numbers that are in the index" to the work instructions). If the same high-severity error repeats even after re-running, a person writes it directly. ("Up to 2 times" is a learning recommendation and has not been tested.)

### 7-6. CH10 work instructions test cases

| Case | Expected behavior |
|---|---|
| T1 (Material 2) | A table + a "Needs confirmation" list, with 0 items not in the notes |
| T2 (Material 4) | Mark the deadline and the owner as "Needs confirmation"; do not make up a name or a date |
| T3 (Material 4) | Do not write sales results that are not in the input material, and report "Not in the material, so not written" |

The author's example in CH10 section 6: in T2, writing "Staff C" as the owner of agenda 2 is a fail (the same phrase from the work instructions is missing from the output format, so it is easy to miss). Have participants find the vague places in their own work instructions themselves.

### 7-7. CH08 K01 and the conflict exercise

The rules in knowledge document K01 should match the five lines of Material 5. The expected decision for the fictional conflict (CH08 Exercise 5): follow K01, which is more recent and is the manager's instruction, and change K03's status to `Retired` and move it to `90_Archive`. A person makes the decision and records it.

### 7-8. CH11, CH13, CH14

- CH11: The expected flowchart is the example in CH11 section 2-2. There must be a human approval point at least before sharing or sending. Exceptions include an empty input, personal information showing up, an AI rule violation, a numbers or quotation mismatch, a service that is unavailable, and no approver.
- CH13: The backup location must be *a place that does not sync* and one whose organization rules were checked. An answer like "I uploaded it to the cloud, so it is backed up" is not complete.
- CH14: The judgment examples in section 9-2.

## 8. Participants with no account, or whose organization's policy does not allow AI use

### 8-1. Alternative paths (no installation or paid account)

| Block | Alternative path |
|---|---|
| 6 (CH06, CH07) | Do not create a Project; write the **design sheet** ([4]) and practice the verification record ([5]) with fictional AI draft A from `sample-ai-output.md`. Mark the record `[Simulated run]` |
| 8 (CH09) | Fact-check table and numeric verification with fictional AI draft B |
| 9 (CH10) | A person *reads only the work instructions*, writes out the test case results by hand, and then, as the checker, confirms whether those results satisfy the rules in the work instructions (finding vague sentences) |
| 11 (CH12) | Error log with fictional AI draft C |
| 12 (CH13) | Plan and checklist as documents. Restore practice only in the practice folder (optional) |
| 13 (CH14) | Path B (simulated run). The aim is Level 1 |

### 8-2. Guidance by situation

| Situation | Guidance |
|---|---|
| No account | Do not recommend signing up (it is not required). Proceed with the alternative path |
| Has an account but it is unclear whether the organization allows it | If it is a personal account that can be used only for fictional data, go as far as `[Live AI run: fictional data]`. Do not use work material until permission is confirmed |
| The organization prohibits AI use | The rules come first. Design and simulated runs only. Do not recommend breaking the rules |
| No cloud account, or the organization's policy does not allow it | CH05 is design only (the table). Skip the optional exercise (real account) |
| No outputs from earlier chapters | Use the setting in `sample-meeting-notes.md` (organizing meeting minutes) and mark it `[Fictional example]` |
| Candidate A is not organizing meeting minutes | As the guidance in CH09 says, read "meeting notes" as swapped for the *fictional input material* of your own task. The answers in this guide apply only to organizing meeting minutes, so coach that participant's results with the same *principles* (two-way comparison, fact check) |

### 8-3. Distinguishing live AI runs from fictional exercises (labeling rule)

Have participants write one of the following on every record (workbook [5][7], CH12 and CH14 records). **Do not use them interchangeably.**

| Label | Meaning | Material you can use |
|---|---|---|
| `[Simulated run]` | Followed along with fictional data and a fictional AI output. Did not ask an AI | Workshop fictional data |
| `[Live AI run: fictional data]` | Asked an AI service using fictional data | Workshop fictional data |
| `[Live AI run: approved work data]` | Asked using real work material that the organization allows and whose tier you have checked | Organization permission + CH03 tier A or masked B. **Not recommended during the workshop** |

Do not call running an AI on fictional data "real work execution."

## 9. Level 1 to 3 criteria (same as CH14 section 2-9)

> These three levels were set by this book for teaching and are not a certification standard. The judgment is the *participant's self-assessment*, not the instructor's verification. A participant who cannot actually run anything because of account or organizational installation limits can still reach Level 1.

| Level | Name | Completion conditions |
|---|---|---|
| Level 1 | Design complete | ① The final workspace map, ② task purpose and scope, ③ folder and material management rules, ④ AI Project setup (a design sheet is also acceptable), ⑤ work instructions, ⑥ task workflow, ⑦ verification checklist, and ⑧ backup and operating rules exist *as documents*, they agree with each other in the connection check sheet (inconsistencies are recorded), and the candidate A task can be explained from the documents alone. Simulated runs may be included |
| Level 2 | Environment set up | Level 1 + it was actually set up in available tools: local folders were actually created / if available, a cloud folder and an AI Project (instructions entered, fictional material uploaded) / the pre-run security check was passed / backup and restore were tried once with fictional files / preparation for a run with fictional data is complete |
| Level 3 | Work executed and verified | Level 2 + real work was done with an AI using approved data (a service and account the organization allows, tier A or masked B from CH03) (`[Live AI run: approved work data]`), and there are the CH12 verification checklist and error log, a human final confirmation record, and a backup |

**Labeling rule:** Write only the single highest level achieved, with the supporting documents. If even one condition is missing, do not write that it was achieved; write "next level in progress." **Do not label someone who finished Level 1 as having finished Level 3.** Running an AI on fictional data alone is not Level 3.

### 9-1. Check questions for the instructor to ask

| Level | Question |
|---|---|
| Level 1 | Tell me the names, versions, and locations of the 8 documents. Where did you record the inconsistencies in the connection check sheet? Could a colleague do candidate A from these documents alone? |
| Level 2 | Which folders did you actually create? Which tools did you set up? Was there a "No" in the pre-run check? Did you try restoring fictional files? |
| Level 3 | Which service and account, and did the organization allow it? What was the tier of the material you entered, and how did you mask it? Where are the verification record and the final confirmation record? |

### 9-2. Judgment examples (the author's examples, CH14 section 6)

| Situation | Judgment |
|---|---|
| The 8 documents exist, the connection check sheet is consistent, and only simulated runs were done. The organization does not allow AI | Level 1 |
| Level 1 + created local folders and did backup and restore with fictional files, put the instructions into an allowed service and ran it with a fictional note | Level 2 (not Level 3 because it is not approved work data) |
| Level 2 + ran it in a service the organization allows with a masked work note, with a verification record, final confirmation, and backup | Level 3 |
| The work instructions are only v01 and there is no verification checklist | Below Level 1 → "design in progress" |

### 9-3. Workshop completion and work environment completion

| | Workshop completion | Work environment completion |
|---|---|---|
| Meaning | Filled in part of the core forms within the workshop time | Meets the Level 2 or Level 3 conditions |
| Evidence | The completed cells in the workbook | Actual setup, backup and restore of fictional files, (Level 3) verification record with approved data |
| Label | `Level 1 in progress (candidate A draft)` | Level 2 / Level 3 (supporting documents) |

## 10. Expected questions and error explanations

| Question / situation | Response |
|---|---|
| "If the AI is wrong, can't I just have it redo it?" | Fix the cause (the input, the work instructions) and re-run. If it repeats, a person writes it directly (CH12). This book does not say AI is never wrong |
| "Can I enter company material into ChatGPT or Claude?" | This book cannot decide that; the organization's rules come first. In the workshop, use fictional data only |
| "I turned off training, so it's safe, right?" | No. Transmission, retention, and training use are separate, and there is a feedback exception (CH03) |
| "I put it in the cloud, isn't that a backup?" | Deletions and edits can spread, and restoring has periods and conditions (CH05, CH13) |
| "Is it safe if I upload it to a Project?" | No. The CH03 tiers and rules still apply |
| "My screen looks different" | It differs by plan, region, app version, and organization settings. Your own screen comes first. The new version of Claude Projects is being rolled out to some users (CH07) |
| "Can I write rules in the Claude Project name?" | Claude cannot see the name and description. Put the rules in the instructions (CH07) |
| "Which is better, ChatGPT or Claude?" | We do not judge which is better. Compare them with the same fictional notes, instructions, and verification criteria |
| "What's the answer?" (during verification) | Do not tell them the answer first. Ask "Where in the source text did you find that sentence?" |
| "How many errors are there?" | Do not tell them. Ask whether they did the full two-way comparison |
| "The work instructions are too long" | Narrow the scope and move the rules to a knowledge document (CH08) |
| "Do we also do Git or harness engineering?" | Not within this workshop's scope. The direction is to split them off as future separate courses |
| "I'm running out of time" | Fill in only some cells and leave the rest as `[Fictional example]` or for later. The goal is not to finish the whole form |
| "I want to write that it worked" | Only as much as there are records for. If there are none, write "not yet measured" |
| "I accidentally entered real information" | Do not hide it; tell the person in charge and delete that conversation (CH03 section 7). Turning off the training setting alone does not delete it |

## 11. Record of differences between the existing manuscript and the workshop materials

We did not edit the existing manuscript, and we did not arbitrarily mix the fictional data of different chapters. The differences below are for the author to decide.

| # | Difference | How the workshop handles it |
|---|---|---|
| 1 | **The CH03 Exercise 2 notes (Material 1) and the CH06 and CH09 notes (Material 2)**: They look like the same meeting before and after masking, but Material 1 writes people and clients with full names (Manager Kim Gana and so on, pseudonyms), says "by next Tuesday," has the vacation in "the first week of November," and does not have agenda 3 or "substitute worker undecided." Material 2 has "by next week," "November vacation," agenda 3, and the substitute worker undecided | We kept both materials as they are and divided their purposes. Material 1 is used only for the CH03 masking exercise, and the reference source text for AI input and verification is Material 2. The instructor should know that even after masking, Material 1 is not exactly the same as Material 2 |
| 2 | **The CH06 notes and the CH09 notes**: CH09 has an amount (KRW 12,500 → KRW 11,800) and a quantity table in agenda 1, and CH06 does not. The fictional AI draft of CH06 (A) and that of CH09 (B) are different texts | Material 2 is the CH09 version (the one with more information). The facts in the CH06 notes do not contradict Material 2. Drafts A and B are kept separate |
| 3 | **CH09 (Week 2 of October 2026) and CH12 (Week 3 of October 2026)**: They are different meetings. The people and clients are in the same fictional world (Manager A, Associate B, Staff C; Client X, Client Y) | We did not mix them, and separated them as Materials 2 and 3 |
| 4 | **CH10 test case T2 and the CH12 notes (Material 3)**: Both are "Week 3 of October 2026" and the agenda is similar, but the attendees (T2 has Manager A and Staff C), whether there is a deadline, and agenda 3 differ | Treated as different materials (Material 4 and Material 3). We tell participants not to read them as the same meeting |
| 5 | **The manager's instruction note in CH08**: The text introduces it as "written down by Gasang Han" | Changed to Staff C in Material 5 with the same content (stated in `sample-meeting-notes.md`). The person in the text's case (Gasang Han) is a person in the textbook's case and differs from the people in the workshop materials (Staff C and so on) |
| 6 | **The blank minutes template**: CH06, CH08, and CH09 use a "blank minutes template," but no place defines its contents | We newly made Material 6 for the workshop (table + Needs confirmation list + written by and checked by). It has the same items as the output format requirements in the text |
| 7 | **The header of the fictional AI drafts**: The text has a label saying "deliberately written wrong" | In the participant-facing `sample-ai-output.md`, to hide the number and location of the errors, we changed the wording to "there are parts that need checking." We stated that it is a fictional output |
| 8 | **The name of ④ in the CH02 form**: CH02 [1] calls ④ "knowledge base," and CH14 writes "work documents and knowledge base" | Workbook block 2 follows CH02's original wording, and `workspace-template.md` follows CH14's original wording. They point to the same box |
| 9 | **Answers exposed in the text**: CH03 (section 6), CH06 (section 6), CH09 (section 6), and CH12 (section 6) have the author's commentary in the text | If learners look at the site or the text together, the answers are visible. See section 12 |
| 10 | **Time**: The total of the time needed in each chapter's text is about 905 minutes | The workshop does only the core exercises, and all times are unverified estimates |
| 11 | **English edition**: Names are rendered in English-friendly form (guide table); all dates, amounts, quantities, decisions and errors are identical to the Korean edition | The English files in en/workshop/ and en/chapters/ use the same renderings, and the Korean files remain the source of truth |

## 12. Remaining cautions

- **Risk of exposing answers:** Some chapters of the textbook contain commentary, so if participants open the textbook alongside, they can see the correct answers for the errors in the fictional AI outputs. This guide and its answers are public material, so they cannot be completely hidden. The website puts the instructor guide behind a separate menu (collapsed by default) and an information page and excludes it from search, but the commentary in section 6 of the text is still there. To hide the answers in a workshop, the facilitator must decide on a way to run it, such as printing with the commentary covered or handing out only the workbook. This package did not edit the text.
- **Copy button:** The code block copy button on the site was not verified in a regular browser (`README.md`). The workbook is a Markdown file, so we recommend printouts or a note-taking tool so you do not depend on copy and paste.
- **Official document changes:** Service screens and policies can change. Re-check before class.
- **Personal information check:** Every person, company, and client in this package is fictional, and the contact `010-0000-0000` is a fake placeholder number. There are no email addresses, real phone numbers, bank accounts, addresses, passwords, or API keys.
- **Before learner testing:** All time and difficulty judgments in this guide are estimates.

## 13. Pilot observation record template (optional)

If you run a test (pilot), write the following for each block and keep it as a working document in `review/`, and do not claim effects before measuring.

```text
Block / chapter | Planned time | Actual start to end | Where they got stuck | Questions | Where the screen differed from the text | Whether an alternative path was used | Cells in the form that could not be filled in
```
