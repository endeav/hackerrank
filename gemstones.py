"""
Problem Statement

John has discovered various rocks. Each rock is composed of various elements, and each element is represented by a lower-case Latin letter from 'a' to 'z'. An element can be present multiple times in a rock. An element is called a gem-element if it occurs at least once in each of the rocks.

Given the list of N rocks with their compositions, display the number of gem-elements that exist in those rocks.

Input Format

The first line consists of an integer, N, the number of rocks. 
Each of the next N lines contains a rock's composition. Each composition consists of lower-case letters of English alphabet.

Constraints 
1=N=100 
Each composition consists of only lower-case Latin letters ('a'-'z'). 
1= length of each composition =100
Output Format

Print the number of gem-elements that are common in these rocks. If there are none, print 0.

Sample Input

3
abcdde
baccd
eeabg
Sample Output

2
"""

import string

def gem(rock, gem_elem, i):
    for key, val in dict.iteritems(gem_elem):
        if key in rock:
            if i == 0:
                gem_elem[key] = 1
            else:
                if val != 0:
                    gem_elem[key] = 1
        else:
            gem_elem[key] = 0
    return gem_elem

N = input()
if (N <= 0) or (N > 100):
    raise ValueError("1 ? N ? 100")
gem_elem = dict(zip(string.lowercase, (0*j for j in range(26))))

for i in range(N):
    rock = raw_input()
    if len(rock) == 0 or len(rock) > 100:
        raise ValueError("Rock lenght not good")
    for val in rock:
        if val.isupper():
            raise ValueError("All letters mush be lowercase")
    gem_elem = dict(gem(rock, gem_elem, i))

count = 0
for key, val in gem_elem.items():
    if val == 1:
        count += 1
print count