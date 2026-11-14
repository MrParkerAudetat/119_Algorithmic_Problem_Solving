# AL05: Filter, Sort, and Search Pipeline

Name: [Parker]
My contribution: [Since this was an individual assignment, I did all the work outside of the help that the AI gave me.]

## Run

Keep all AL05 Python files together, then run:

    py -3.14 main.py
    py -3.14 test_assignment.py

## Pipeline and Work Notes

- Pipeline: source tickets -> filter -> age display and ID search views -> lookup.
- One request: filter the source and use linear search on the selection. If an
  age-ordered display is needed, sort that one as well. Building an ID search view adds both
  sorting and storage setup for that specific lookup.
- Repeated requests: filter and sort once, retain the ID-ordered view, and use
  binary search for each lookup. The views take extra storage and must be
  rebuilt when the eligibility rule or relevant ticket data changes.
- Issued change: raising the minimum from 4 to 7 days leaves tickets 403 and 405.
  The filter is called with a different threshold; sorting and searching
  algorithms stay the same.
- Copying and stability: the views are separate lists sharing ticket
  dictionaries. Equal ages keep their order from the input.

## AI Assistance
I used the built-in AI to help draft and explain the pipeline and tests. It also
identified an ineffective input-preservation assertion and then helped me fix it by checking against the saved copy. After having the AI check it over one last time for errors, I ran the two files and both were successful. It did also help me give a nice layout for the README, making it so I wouldn't spend an unnecessary amount of time trying to figure out how to make it look. I personally added the display and search ID output for the empty 8-day selection in the main.py file. 

## File Assistance
I did use the AL05 starter and support modules that were given out. I copied my personal AL04 search functions into the local search module instead of using the recovery code.

## Instructor comments: