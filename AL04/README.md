# AL04: Search Contracts and Correctness

Name: [Parker]
My contribution: [Since this was an individual assignment, I did everything besides what the AI did which is explained down in the AI assistance section.]


## Run

py -3.14 main.py
py -3.14 test_assignment.py

## Notes

- Linear search checks tickets one at a time. Binary search needs tickets
  sorted by the same key used for the search.
- Binary search misses T401 in the original list because it discards
  part of an unsorted list where T401 happens to be.
- Positions can differ because each position belongs to the list searched.
  For duplicate categories, either matching ticket is acceptable.
- Linear search can check every ticket. Binary search narrows the search,
  but preparing and storing a sorted view also has a cost.

## AI Assistance

I used the built-in AI to help explain, draft, and helped me go over the code to check for anything I may have missed. While doing the code, I changed a variable and a statement. The variable it gave me was "middle", I changed it to "mid". It also recommended I used an if statement next to "comparison < 0:", I decided to change that to an else if statement. These two changes were made in the main.py file.
