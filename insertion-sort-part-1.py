"""
Problem Statement

Sorting 
One common task for computers is to sort data. For example, people might want to see all their files on a computer sorted by size. Since sorting is a simple problem with many different possible solutions, it is often used to introduce the study of algorithms.

Insertion Sort 
These challenges will cover Insertion Sort, a simple and intuitive sorting algorithm. We will first start with an already sorted list.

Insert element into sorted list 
Given a sorted list with an unsorted number V in the rightmost cell, can you write some simple code to insert V into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. The goal of this challenge is to follow the correct order of insertion sort.

Guideline: You can copy the value of V to a variable and consider its cell "empty". Since this leaves an extra cell empty on the right, you can shift everything over until V can be inserted. This will create a duplicate of each value, but when you reach the right spot, you can replace it with V.

Input Format 
There will be two lines of input:

s - the size of the array
ar - the sorted array of integers
Output Format 
On each line, output the entire array every time an item is shifted in it.

Constraints 
1=s=1000 
-10000=V=10000,V?ar

Sample Input

5
2 4 6 8 3
Sample Output

2 4 6 8 8 
2 4 6 6 8 
2 4 4 6 8 
2 3 4 6 8 
"""

import sys

s = int(raw_input())
ar = map(int, (raw_input()).split(" "))
i = s-1
v = ar[s-1]

for i in range(s-1, -1, -1):
    if (v < ar[i-1]):
        # in case v is the min in the list 
        ar[i] = ar[i-1] if i >= 1 else v
    if (v >= ar[i-1]):
        ar[i] = v
        print " ".join(map(str, ar))
        break
    print " ".join(map(str, ar))
