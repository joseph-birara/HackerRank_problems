

**Insertion Sort - Part**

**1**

**Sorting**

One common task for computers is to sort data. For example, people might want to see all their files on a

computer sorted by size. Since sorting is a simple problem with many different possible solutions, it is

often used to introduce the study of algorithms.

**Insertion Sort**

These challenges will cover Insertion Sort, a simple and intuitive sorting algorithm. We will first start with

an already sorted list.

**Insert element into sorted list**

Given a sorted list with an unsorted number in the rightmost cell, can you write some simple code to

insert into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. The goal of this

challenge is to follow the correct order of insertion sort.

Guideline: You can copy the value of to a variable and consider its cell "empty". Since this leaves an

extra cell empty on the right, you can shift everything over until

can be inserted. This will create a

duplicate of each value, but when you reach the right spot, you can replace it with .

**Input Format**

There will be two lines of input:

\- the size of the array

\- the array containing

sorted integers and unsorted integer in the rightmost cell

**Output Format**

On each line, output the entire array every time an item is shifted in it.

**Constraints**

**Sample Input**

5

2 4 6 8 3

**Sample Output**

2 4 6 8 8

2 4 6 6 8

2 4 4 6 8

2 3 4 6 8

**Explanation**

is removed from the end of the array.

In the st line

In the nd line

In the rd line

In the th line

, so is shifted one cell to the right.

, so is shifted one cell to the right.

, so is shifted one cell to the right.

, so is placed at position .

**Task**





Complete the method insertionSort which takes in one parameter:

\- an array with the value in the right-most cell.

**Next Challenge**

In the [next](https://www.hackerrank.com/challenges/insertionsort2)[ ](https://www.hackerrank.com/challenges/insertionsort2)[Challenge](https://www.hackerrank.com/challenges/insertionsort2), we will complete the insertion sort itself!

