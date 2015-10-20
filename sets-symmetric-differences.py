"""
Problem Statement

Lets learn about a new datatype 'sets'! You are given two set of integers M and N and you have to print their symmetric difference in ascending order. The first line of input contains value of M followed by M integers, then value of N followed by N integers. Symmetric difference between M and N mean those values which either exist in M or in N but not in both.

Input Format

Value of M followed by M integers, then value of N followed by N integers.

Output Format

Integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12
"""

mLen = raw_input()
mString = raw_input()

nLen = raw_input()
nString = raw_input()

mArr = mString.split()
mList = list(map(int, mArr))
mSet = set()
mSet.update(mList)

nArr = nString.split()
nList = list(map(int, nArr))
nSet = set()
nSet.update(nList)

mDiff = mSet.difference(nSet)
nDiff = nSet.difference(mSet)

mnUnion = mDiff.union(nDiff)
resultList = sorted(list(mnUnion))

for item in resultList:
    print item
