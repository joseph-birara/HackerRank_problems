

**Sorting: Bubble Sort**

Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {

for (int j = 0; j < n - 1; j++) {

// Swap adjacent elements if they are in decreasing order

if (a[j] > a[j + 1]) {

swap(a[j], a[j + 1]);

}

}

}

Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once

sorted, print the following three lines:

\1. Array is sorted in numSwaps swaps. , where

\2. First Element: firstElement , where

\3. Last Element: lastElement , where

is the number of swaps that took place.

is the first element in the sorted array.

is the last element in the sorted array.

**Hint:** To complete this challenge, you must add a variable that keeps a running tally of all swaps that

occur during execution.

For example, given a worst-case but small array to sort:

we go through the following steps:

swap

a

0

1

2

3

[6,4,1]

[4,6,1]

[4,1,6]

[1,4,6]

It took swaps to sort the array. Output would be

Array is sorted in 3 swaps.

First Element: 1

Last Element: 6

**Function Description**

Complete the function countSwaps in the editor below. It should print the three lines required, then

return.

countSwaps has the following parameter(s):

a: an array of integers .

**Input Format**

The first line contains an integer, , the size of the array

The second line contains space-separated integers

.

.

**Constraints**

**Output Format**





You must print the following three lines of output:

\1. Array is sorted in numSwaps swaps. , where

\2. First Element: firstElement , where

\3. Last Element: lastElement , where

**Sample Input 0**

is the number of swaps that took place.

is the first element in the sorted array.

is the last element in the sorted array.

3

1 2 3

**Sample Output 0**

Array is sorted in 0 swaps.

First Element: 1

Last Element: 3

**Explanation 0**

The array is already sorted, so swaps take place and we print the necessary three lines of output shown

above.

**Sample Input 1**

3

3 2 1

**Sample Output 1**

Array is sorted in 3 swaps.

First Element: 1

Last Element: 3

**Explanation 1**

The array is not sorted, and its initial values are:

. The following swaps take place:

\1.

\2.

\3.

At this point the array is sorted and we print the necessary three lines of output shown above.

