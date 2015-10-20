# Problem Statement
# 
# You are given an array of integers of size N. You need to print the sum of the elements in the array.
# 
# Input Format 
# The first line of input consists of an integer N. The next line contains N space-separated integers contained inside the array.
# 
# Constraints 
# 1=N=1000 
# 0=A[i]=1000
# 
# Output Format 
# Output a single value equal to the sum of the elements in the array.
# 
# Sample Input
# 
# 6
# 1 2 3 4 10 11
# Sample Output
# 
# 31

T <- suppressWarnings(readLines(file("stdin")))
T <- strsplit(T, " ")
Ti <- as.numeric(T[[1]])
Tnew <- T[-1]
out <- sum(as.numeric(Tnew[[1]]))
write(as.character(out), stdout())
