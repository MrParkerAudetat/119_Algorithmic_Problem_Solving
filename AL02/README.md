## Function First_ID(records)
This function only examines one item.  We believe that it is O of 1 for the reasons of it is a constant of scanning only one ID. 
---
## Function All_IDs(records)
This function examines every ID present in the code. We believe that it is O(n) because it runs through every record available only once.
---
## Function Ordered_Pairs(records)
This function examines every ID that is present twice and puts them into pairs and visits them. We believe that it is O(n^2) because it's running through the IDs twice and it creating ordered pairs in pairs of two.

---
## Functions Halving_Sizes(size)
This function examines every ID then repeatedly goes through them and reduces the remaining size of them. We believe that it is logarithmic, because it is not constant, linear, nor is it quadratic. 