# Number Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1234
# 123
# 12
# 1
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Sample Input :
# 5
# Sample Output :
# 12345
# 1234
# 123
# 12
# 1


n = int(input())
i=n
while i>0:
    j=1
    k=1
    while j<=i:
        print(k,end="")
        j+=1
        k+=1
    print("")
    i-=1
