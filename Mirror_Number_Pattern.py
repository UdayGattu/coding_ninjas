# Code : Mirror Number Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4




# The dots represent spaces.


# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 50
# Sample Input 1:
# 3
# Sample Output 1:
#       1 
#     12
#   123
# Sample Input 2:
# 4
# Sample Output 2:
#       1 
#     12
#   123
# 1234

n=int(input())
i=1
while i<=n:
    j=1
    k=n-i
    while k>0:
        print(" ",end="")
        k-=1
    while j<=i:
        print(j,end="")
        j+=1
    print("")
    i+=1
