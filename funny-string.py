"""
Problem Statement

Suppose you have a string S which has length N and is indexed from 0 to N-1. String R is the reverse of the string S. The string S is funny if the condition |Si-Si-1|=|Ri-Ri-1| is true for every i from 1 to N-1.

(Note: Given a string str, stri denotes the ascii value of the ith character (0-indexed) of str. |x| denotes the absolute value of an integer x)

Input Format

First line of the input will contain an integer T. T testcases follow. Each of the next T lines contains one string S.

Constraints

1<=T<=10
2<=length of S<=10000
Output Format

For each string, print Funny or Not Funny in separate lines.

Sample Input

2
acxz
bcxz
Sample Output

Funny
Not Funny
"""

import sys
import math

T = int(raw_input())
for i in range(0, T):
    myString = raw_input()
    ms = list(myString)
    msr = ms[::-1]
    areEqual = [0] * (len(ms)-1)

    for j in range(1, len(ms)):
        checkMS = math.fabs(ord(ms[j]) - ord(ms[j-1]))
        checkMSR = math.fabs(ord(msr[j]) - ord(msr[j-1]))
        if checkMS == checkMSR:
            areEqual[j-1] = 1

    if 0 in areEqual:
        print 'Not Funny'
    else:
        print 'Funny'
