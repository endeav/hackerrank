"""
Problem Statement

Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)

After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

Given a sentence s, tell Roy if it is a pangram or not.

Input Format Input consists of a line containing s.

Constraints 
Length of s can be at most 103 (1=|s|=103) and it may contain spaces, lower case and upper case letters. Lower case and upper case instances of a letter are considered the same.

Output Format Output a line containing pangram if s is a pangram, otherwise output not pangram.

Sample Input #1

We promptly judged antique ivory buckles for the next prize    
Sample Output #1

pangram
Sample Input #2

We promptly judged antique ivory buckles for the prize    
Sample Output #2

not pangram
"""

import sys
sentance = raw_input()
sentanceList = list(sentance)
# clean list of empty spaces
sentanceListClean = [x for x in sentanceList if x != ' ']
# make all letters lowercase
sentanceLowercase = map(lambda x:x.lower(), sentanceListClean)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabetBool = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
isPangram = 1

for i in sentanceLowercase:
    pos = alphabet.index(i)
    if alphabetBool[pos] == 0:
        alphabetBool[pos] = 1
    
if 0 in alphabetBool:
    print 'not pangram'
else:
    print 'pangram'