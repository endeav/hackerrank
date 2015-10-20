"""
Problem Statement

Watson gives two integers (A and B) to Sherlock and asks if he can count the number of square integers between A and B (both inclusive).

Note: A square integer is an integer which is the square of any integer. For example, 1, 4, 9, and 16 are some of the square integers as they are squares of 1, 2, 3, and 4, respectively.

Input Format 
The first line contains T, the number of test cases. T test cases follow, each in a new line. 
Each test case contains two space-separated integers denoting A and B.

Output Format 
For each test case, print the required answer in a new line.

Constraints 
1=T=100 
1=A=B=109

Sample Input

2
3 9
17 24
Sample output

2
0
"""

import sys
import math

# Fetch the input
n = int(raw_input())

for i in range(0,n):
    x,y = map(int, raw_input().split(" "))
    xSqrt = int(math.sqrt(x))
    ySqrt = int(math.sqrt(y))
    dif = ySqrt - xSqrt
    if (x == 1) or (math.modf(math.sqrt(x))[0] == 0):
        print dif + 1
    else:
        print dif
