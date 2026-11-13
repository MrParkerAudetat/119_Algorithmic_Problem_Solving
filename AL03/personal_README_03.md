# AL03: Ticket Registry, Queue, and Undo

Name: Parker
Partners: Ty
Shared repository: https://github.com/MrParkerAudetat/119_Algorithmic_Problem_Solving_ALO3
My contribution: I helped come up with ideas and wrote a few functions down in the main.py file. I do not remember which ones they were exactly but I think it was indexed_lookup, update_priority, build_index, and scan_lookup. I also went through the main.py file and replaced all "equipment" ids/text that I found necessary with tickets to keep it more inline with what the assignment was about.

## Run

Keep main.py, test_assignment.py, ticket_data.py, ticket_display.py,
console_style.py, and any other imported modules together.

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

## Operation Comparison

One short reason per row is enough. Compare list and dictionary behavior;
do not implement every operation twice or maintain two live stores.

| Operation | Representation fit / reason |
| --- | --- |
| Find one ticket by ID | Using a dictionary would be quicker to use because the user could just look up the ticket they want with its ID (for example ticket_id_28). Meanwhile if they were to use a list, it would be slower because it would have to go through 27 different IDs before it got to ticket_id_28.|
| Update one ticket's priority |Using a dictionary behavior would make updating a ticket's priority quicker because the user can directly search for the specific ID they want to update. But if a list behavior were to be used, it would have to be through all the other IDs before it could land on the specific ID the user would want (for example 28), making it a slower process.|
| Select tickets in a category |There really is no difference because regardless of which one were used because the user would have to check each ticket.|

## Work Notes and Reflections

Append brief observations, debugging challenges, changes, and learnings.

- Processing and undo: [When I processed the two tickets and pressed undo, the second processed ticket went back to the waiting list.]
- Contract or snapshot learning: [Even though I changed the ticket, it stayed the same.]

These can be short bullets, not an essay or separate evidence document.

## Assistance

[I had AI help explain to me what the program was about when I was still confused about it on Monday. I also had it help with the "contract or snapshot learning" reflection because I was a bit confused on that as well.]

## Instructor Comments

[Reserved for instructor feedback.]
