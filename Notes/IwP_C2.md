# Chapter 2: Recursion vs. Iteration? (https://inventwithpython.com/recursion/chapter2.html)

### What is the concept being introduced?
Fibonacci sequence, factorial functions.


### Why is it (the concept) important, and what problem does it solve?

Problem(s):
* involves tree-like structure.
* involves backtracking
* not deeply recursive asa to potentially cause a stack overflow.

### When or how would I use it?
* Number of ways that exist to order things.


### What parts of it do I not yet understand?
Using it in coding.

## Vocab
n!: Factorial of n.
Example: 5! (5 x 4 x 3 x 2 x 1) = 120

power rule: (a^m)^n =a^mn

product rule: a^n x a^m =a^n+m
 * Includes a^n x a +a^n + 1

 self-similar: branching points that look similar to the root of a smaller subtree.

 maze: Branching points occur wherever you must pick one of many paths to follow.

 Fibonacci number: Sum of the previous two Fibonacci numbers
 * Example: 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, etc.

# Practice 

## Practice Questions

Test your comprehension by answering the following questions:
### What is 4! (that is, the factorial of 4)?
4! = (1 x 2 x 3 x 4) = 24

### How can you use the factorial of (n – 1) to calculate the factorial of n?


### What is the critical weakness of the recursive factorial function?


### What are the first five numbers of the Fibonacci sequence?


### What two numbers do you add to get the nth Fibonacci number?


### What is the critical weakness of the recursive Fibonacci function?


### What does an iterative algorithm always use?


### Is it always possible to convert an iterative algorithm into a recursive one?


### Is it always possible to convert a recursive algorithm into an iterative one?


### Any recursive algorithm can be performed iteratively by using what two things?


### What three features do programming problems that are suitable to recursive solutions have?


### When is recursion required to solve a programming problem?


## Practice Projects

For practice, write a function for each of the following tasks:

### Iteratively calculate the sum of the integer series from 1 to n. This is similar to the factorial() function, except it performs addition instead of multiplication. For example, sumSeries(1) returns 1, sumSeries(2) returns 3 (that is, 1 + 2), sumSeries(3) returns 6 (that is, 1 + 2 + 3), and so on. This function should use a loop instead of recursion. Take a look at the factorialByIteration.py program in this chapter for guidance.


### Write the recursive form of sumSeries(). This function should use recursive function calls instead of a loop. Look at the factorialByRecursion.py program in this chapter for guidance.


### Iteratively calculate the sum of the first n powers of 2 in a function named sumPowersOf2(). The powers of 2 are 2, 4, 8, 16, 32, and so on. In Python, these are calculated with 2 ** 1, 2 ** 2, 2 ** 3, 2 ** 4, 2 ** 5, and so on, respectively. In JavaScript, these are calculated with Math.pow(2, 1), Math.pow(2, 2), and so on. For example, sumPowersOf2(1) returns 2, sumPowersOf2(2) returns 6 (that is, 2 + 4), sumPowersOf2(3) returns 14 (that is, 2 + 4 + 8), and so on.


### Write the recursive form of sumPowersOf2(). This function should use recursive function calls instead of a loop.
