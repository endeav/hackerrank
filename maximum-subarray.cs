/*
Problem Statement

Given an array A={a1,a2,…,aN} of N elements, find the maximum possible sum of a

Contiguous subarray
Non-contiguous (not necessarily contiguous) subarray.
Empty subarrays/subsequences should not be considered.

Input Format

First line of the input has an integer T. T cases follow. 
Each test case begins with an integer N. In the next line, N integers follow representing the elements of array A.

Constraints:

1=T=10
1=N=105
-104=ai=104
The subarray and subsequences you consider should have at least one element.

Output Format

Two, space separated, integers denoting the maximum contiguous and non-contiguous subarray. At least one integer should be selected and put into the subarrays (this may be required in cases where all elements are negative).

Sample Input

2 
4 
1 2 3 4
6
2 -1 2 3 4 -5
Sample Output

10 10
10 11
*/
using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        int T = Int32.Parse(Console.ReadLine());
        var aList = new List<int[]>();
            for (int i = 0; i < T; i++) {
                int len = int.Parse(Console.ReadLine());
                string[] myString = Console.ReadLine().Split(' ');
                int[] numbers = Array.ConvertAll<string, int>(myString, int.Parse);
                
                aList.Add(numbers);
            }
            foreach (var item in aList) {
            
                var maxSum = -100000;
                var sum_so_far = -100000;
                var sum2 = -100000;
                for (int i = 0; i < item.Length; i++) {
                    // sum type 1
                    sum_so_far = Math.Max(sum_so_far + item[i], item[i]);
                    maxSum = Math.Max(sum_so_far, maxSum);
                    // sum type 2
                    sum2 = Math.Max(sum2, Math.Max(item[i], sum2 + item[i]));
                }
                
                Console.WriteLine("{0} {1}", maxSum, sum2);
                
            }
    }
}