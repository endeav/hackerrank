/*
Problem Statement

James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

He can reduce the value of a letter, e.g. he can change d to c, but he cannot change c to d.
In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter becomes a. Once a letter has been changed to a, it can no longer be changed.
Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.

Input Format

The first line contains an integer T, i.e., the number of test cases. 
The next T lines will contain a string each. The strings do not contain any spaces.

Constraints 
1=T=10 
1= length of string =104 
All characters are lower case English letters.

Output Format

A single line containing the number of minimum operations corresponding to each test case.
Sample Input

4
abc
abcba
abcd
cba
Sample Output

2
0
4
2
*/

using System;

class Palindrom
{
    public static void Main()
    {
        string line;
        int T = Int32.Parse(Console.ReadLine());
        for (int i = 1; i <= T; i++)
        { 
            line = Console.ReadLine();
            int n = line.Length;
            int sum = 0;
            int middle = 0;
            if (n % 2 == 0) 
            {
                middle = n/2;
            }
            else
            {
                middle = (int)n/2;
            }
            for(int k = 0; k < middle; k++)
            {
                int tmp = (int)line[k] - (int)line[n-k-1];
                if (tmp < 0)
                {
                    tmp = (-1) * tmp;
                }
                sum += tmp;
            }
            Console.WriteLine(sum);
        }
    }
}
