# Workshop fictional meeting materials (sample-meeting-notes)

> **All of this material is fictional and for teaching only.** The company "Example Trading Co.", the team, the people, the clients, the schedules, and the amounts have nothing to do with real ones. It contains no real customer information, personal information, or company secrets. The contact number `010-0000-0000` is a *fake placeholder number*.
>
> **How to use it.** In the workshop, use only the materials in this document as input to AI services or to the fictional AI outputs. Do not use your own real meeting notes or work materials. Each item says *which exercise in which chapter it is used for*. This document has no answers or explanations.

## 0. Setting of this fictional world

- Company: the **Example Trading Co.** sales team (all fictional)
- People (masked labels): **Manager A**, **Associate B**, **Staff C**. In Material 1, the *pre-masking* labels of the same meeting appear: Manager Kim Gana, Associate Lee Dara, Staff Park Maba.
- Clients: **Client X** (Oreum Trading in Material 1), **Client Y**
- Basic task (candidate A): organizing meeting minutes. Purpose (the CH01 example): reduce the burden of repetitive document work and reduce omissions and errors

| Material | Name | Where it is used |
|---|---|---|
| Material 1 | Sales meeting notes — before masking | CH03 Exercise 2 (masking to make it safe) |
| Material 2 | Sales meeting notes — masked version + quantity table | CH06 and CH07 first run, CH09, CH10 test case T1 |
| Material 3 | Next meeting notes (Week 3 of October) | CH12 |
| Material 4 | Work instructions test cases T2, T3 | CH10 Exercise 2 |
| Material 5 | Minutes writing memo (manager's instructions) | CH08 Exercise 3 |
| Material 6 | Blank meeting minutes template | CH06 and CH07 project materials, CH08 |

---

## Material 1. Sales meeting notes — before masking (CH03 Exercise 2)

*This is for practicing masking names, amounts, and contact details. Do not enter this material into an AI service. Use only the masked result in the next step.*

```text
Sales team meeting notes, Week 2 of October 2026 (fictional)
Attendees: Manager Kim Gana, Associate Lee Dara, Staff Park Maba
Agenda 1) Lowering the per-unit price of parts delivered to Oreum Trading from KRW 12,500 to KRW 11,800
 - Manager Kim Gana opposed the cut. Associate Lee Dara will send a revised proposal to the Oreum Trading contact (010-0000-0000) by next Tuesday
Agenda 2) Adjusting Staff Park Maba's vacation schedule
 - Staff Park Maba requested vacation in the first week of November
```

## Material 2. Sales meeting notes — masked version + quantity table (CH06, CH07, CH09, CH10)

*This is the same meeting written with masked labels. In the workshop, this Material 2 is the **reference source text** for AI input and verification.*

```text
Sales meeting notes, Week 2 of October 2026 (fictional)
Attendees: Manager A, Associate B, Staff C
Item 1) Lowering the unit price of the parts supplied to Client X from KRW 12,500 to KRW 11,800 per unit
 - Manager A opposed the cut. Associate B will send a revised proposal to Client X's contact by next week
Item 2) Adjusting Staff C's vacation schedule
 - Staff C applied for vacation in November. A substitute worker has not been decided
Item 3) Next meeting schedule
 - The next meeting will be in the fourth week of October; the date is undecided

[Reference table: Client X monthly delivery quantity (fictional)]
Month | Quantity (units)
July | 1,200
August | 1,350
September | 1,100
```

## Material 3. Next meeting notes — Week 3 of October (CH12)

```text
Sales meeting notes, Week 3 of October 2026 (fictional)
Attendees: Manager A, Associate B, Staff C
Agenda 1) Introduction materials for the November new product
 - Staff C will write the draft by October 30, and Associate B will review it
Agenda 2) Training schedule
 - One day in the second week of November, but the date is undecided. The owner has not been decided
Agenda 3) Client Y inquiry
 - Client Y asked about a delivery delay. Manager A will reply by phone on October 25. The reason for the delay has not yet been confirmed
Reference rule: Minutes Writing Rules K01 (K01 is the only document in the index)
```

## Material 4. Work instructions test cases T2, T3 (CH10 Exercise 2)

*Test case T1 uses Material 2 as it is.*

```text
[Test case T2: missing information]
Meeting notes for Week 3 of October 2026 (fictional)
Attendees: Manager A, Staff C
Agenda 1) Create new product introduction material
 - Staff C will write it. The deadline was not mentioned
Agenda 2) Training schedule
 - It was agreed to do it, but neither the owner nor the date was decided
```

```text
[Test case T3: out-of-scope request]
With the notes from Material 2: "Please also put last quarter's sales results in the meeting minutes."
```

## Material 5. Minutes writing memo — manager's instructions (CH08 Exercise 3)

```text
Minutes writing memo (fictional; the sales team manager's instructions at Example Trading Co., noted by Staff C)
- Write decisions, owners, deadlines, and open items in the minutes as a table.
- If an owner or deadline was not set in the meeting, write "Needs confirmation."
- Write names and amounts as they appear in the notes and do not change them on your own.
- Share the draft within 3 days after the meeting.
- Share the final minutes only after the manager has checked them.
```

*In the body of CH08, this memo is introduced as "noted by Gasang Han." In this workshop material it is unified under the fictional label Staff C; the content is the same.*

## Material 6. Blank meeting minutes template (for the workshop)

*This is the output format required in CH06 and CH09 (a table + a list of items needing confirmation), turned into a blank template.*

```text
Meeting minutes (Meeting name: / Date and time: / Attendees: )
| Item | Decision | Owner | Deadline |
|---|---|---|---|
| | | | |
Open items:
Items that need confirmation:
Prepared by: (name or role)   Checked by: (approver's role)   Date checked:
```
