# Chapter 1: Overview of Algorithms
## Vocabulary
### Algorithm: Set of rules that carry out some calculations to solve a problem.
•	Designed to yield results for any valid input according to precisely defined instructions.

### •	3 design concerns of an algorithm:
1.	Is this algorithm producing the result we expected?
2.	Is this the most optimal way to get these results?
3.	How is the algorithm going to perform on larger datasets?

### Phases of an algorithm:
### 1.	Development phase:
•	Design phase: Architecture, logic and implementation details are envisioned and documented.
o	Is an iterative process that compares different candidate algorithms.
### • Coding phase: Designed algorithm is converted into a computer program.
### Functional requirements: 
Requirements that directly specify expected features of the solutions.

•	Detail expected behavior of the solution.
Non-functional requirements: Requirements that are about the performance scalability, usability, and accuracy of the algorithm.

•	Also establish expectations of the data.

### Data-intensive algorithms: Designed to deal with a large amount of data.
•	Is expected to have relatively simplistic processing requirements.

•	A good example of this is a comprehension algorithm being applied to a huge file.

### Compute-intensive algorithms: Have considerable computing requirements, but do not involve large amounts of data.

•	Example would be a very large prime number.

### Data and compute-intensive algorithms:
Algorithms that deal with large amounts of data and also have considerable computing requirements.

### Volume: 
Expected size of the data that the algorithm will process.

### Velocity: 
Expected rate of new data generation when the algorithms is used.

•	It can be zero.

### Variety: 
Quantifies how many different typers of data the designed algorithms is expected to deal with.

### Examples of use cases involving 3 different types of data:
-	A simple data-processing use case where input data is a .csv file.
o	Volume, velocity, and variety of data will be low.

-	Input data is the live stream of a security video camera.
o	Volume, velocity, and variety of data will be quite high and should be kept in mind while designing an algo for it.

-	Use case of a typical sensor network (data source is a mesh of temperature sensors installed in a large building).
o	Velocity of data is typically high, volume is expected to be quite low.

### Complexity theory: 
Study of how complicated algorithms are. To be useful, any algorithm should have 3 key features:
1.	Should be correct.
2.	Should be understandable.
3.	 Should be efficient.

There are two possible types of analysis to quantify the complexity of an algorithm:
### •	Space complexity analysis: 
Estimates the runtime memory requirements needed to execute the algorithm.
### •	Time complexity analysis: 
Estimates time algorithm will take to run.
