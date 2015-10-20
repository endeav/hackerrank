"""
Problem Statement

The Utopian Tree goes through 2 cycles of growth every year. The first growth cycle occurs during the spring, when it doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter.

Now, a new Utopian Tree sapling is planted at the onset of spring. Its height is 1 meter. Can you find the height of the tree after N growth cycles?

Input Format

The first line contains an integer, T, the number of test cases. 
T lines follow; each line contains an integer, N, that denotes the number of cycles for that test case.

Constraints 
1=T=10 
0=N=60
Output Format

For each test case, print the height of the Utopian Tree after N cycles. Each line thus has to contain a single integer, only.

Sample Input

3
0
1
4
Sample Output

1
2
7
"""

def utopian(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n % 2 == 0:
        return utopian(n-1) + 1
    else:
        return 2 * utopian(n-1)


T = input()    

if (T < 1) or (T > 10):
    raise ValueError("T should be: 1 <= T <= 10")    
else:
    for t in range(T):
        try:
            N = input()
            if (N < 0) or (N > 60):
                raise ValueError("N should be: 1 <= N <= 60")
            else:
                print utopian(N)
        except EOFError:
            print "Insert the right amount of cycles"
            break
