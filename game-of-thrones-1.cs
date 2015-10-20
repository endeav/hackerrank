/*
Problem Statement

Dothraki are planning an attack to usurp King Robert's throne. King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.

But, to lock the door he needs a key that is an anagram of a certain palindrome string.

The king has a string composed of lowercase English letters. Help him figure out whether any anagram of the string can be a palindrome or not.

Input Format 
A single line which contains the input string.

Constraints 
1= length of string =105 
Each character of the string is a lowercase English letter.

Output Format 
A single line which contains YES or NO in uppercase.

Sample Input : 01

aaabbbb
Sample Output : 01

YES
*/
using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        string myString = Console.ReadLine();
            char[] myChar = myString.ToCharArray();
            Array.Sort(myChar);
            int odds = 0;
            int count = 1;
            for (int i = 1; i < myChar.Length; i++) {
                if (myChar[i] == myChar[i-1]) {
                    count++;
                }
                else {
                    if (count % 2 == 0) {
                        // reset the counter
                        count = 1;
                    }
                    else {
                        odds++;
                        count = 1;
                        if (odds != 0 && odds != 1) {
                            count = -1;
                            Console.WriteLine("NO");
                            break;
                        }
                    }
                }
            }
            if (count != -1) {
                Console.WriteLine("YES");
            }
    }
}