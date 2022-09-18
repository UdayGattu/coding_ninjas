# Code : Star Pattern
# Send Feedback
# Print the following pattern
# Pattern for N = 4



# The dots represent spaces.



# Input Format :
# N (Total no. of rows)
# Output Format :
# Pattern in N lines
# Constraints :
# 0 <= N <= 50
# Sample Input 1 :
# 3
# Sample Output 1 :
#    *
#   *** 
#  *****
# Sample Input 2 :
# 4
# Sample Output 2 :
#     *
#    *** 
#   *****
#  *******

n=int(input())
i=1
while i<=n:
    k=n-i
    j=1
    p=i-1
    while k>0:
        print(" ",end="")
        k-=1
    while j<=i:
        print("*",end="")
        j+=1
    while p<=i and p!=0:
        print("*",end="")
        p-=1
    print("")
    i+=1
