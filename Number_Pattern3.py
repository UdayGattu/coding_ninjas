# Number Pattern 3
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 11
# 121
# 1221
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Sample Input :
# 5
# Sample Output :
# 1
# 11
# 121
# 1221
# 12221

n= int(input())
if n>0:
    print(1)
i=1
while i<n:
    print(1,end="")
    j=1
    while j<=i-1:
        print(2,end="")
        j+=1
    print(1)
    i+=1
