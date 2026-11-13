# README
Name: Parker
Partner(s): Aiden
Shared repository: https://github.com/AidenCanon/AL02-Parker-and-Aiden
My contribution: I typed out the Functions Analysis section and helped with the examinations for the functions and what Big-0 was used. I also helped analyze the Main.py file and Testcase.py file. I typed out the index_lookup function. 

## Run

Keep main.py, test_assignment.py, catalog_data.py, growth_examples.py,
and any other imported modules together.

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

# Work Notes and Reflections

## Functions Analysis

## Function First_ID(records)
This function only examines one item. I believe that it is O of 1 for the reasons of it is a constant of scanning only one ID. 
---
## Function All_IDs(records)
This function examines every ID present in the code. I believe that it is O(n) because it runs through every record available only once.
---
## Function Ordered_Pairs(records)
This function examines every ID that is present twice and puts them into pairs and visits them. I believe that it is O(n^2) because it's running through the IDs twice and it creating ordered pairs in pairs of two.
---
## Functions Halving_Sizes(size)
This function examines every ID then repeatedly goes through them and reduces the remaining size of them. I believe that it is logarithmic, because it is not constant, linear, nor is it quadratic. 

## Recommended Approach/Observations
1. There is no need to create a new index. The index that is given is enough because there are only 4 records so it will not take that wrong to go through each record, even if it has to be ran multiple times for whatever reason.

2. The best approach would be to create multiple repositories for that because the bigger the records are, the more important having an index would be to keep those. 

3. Building an index means looking through the books and making a list that connects to book id thats stored. It's way more convenient (despite taking up additional storage) than it would be compared to not having an index because without an index, it would have to go through every single ID again starting from the first one. 

## AI Assistance
* I did not use any AI to help write out the index_lookup function nor any other pieces of code.
* We did have AI help reassure our answers  when we collaborated for the function and big-O examination were correct. After asking it to verify each one, it told us it was correct. 

## Instructor's Feedback
