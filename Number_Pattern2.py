# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 11
# 202
# 3003
# Input format :
# Integer N (Total no. of rows)
# Contraints:
# 1 <= n <= 50
# Output format :
# Pattern in N lines
# Sample Input :
# 5
# Sample Output :
# 1
# 11
# 202
# 3003
# 40004

n=int(input())
if n>0:
    print(1)
i=1
while i<n:
    print(i,end="")
    j=1
    while j<=i-1:
        print(0,end="")
        j+=1
    print(i)
    i+=1
