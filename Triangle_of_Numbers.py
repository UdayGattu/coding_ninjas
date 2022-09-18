# Code : Triangle of Numbers
# Send Feedback
# Print the following pattern for the given number of rows.
# Pattern for N = 4



# The dots represent spaces.



# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints :
# 0 <= N <= 50
# Sample Input 1:
# 5
# Sample Output 1:
#            1
#          232
#        34543
#      4567654
#    567898765
# Sample Input 2:
# 4
# Sample Output 2:
#            1
#          232
#        34543
#      4567654

n = int(input())
i=1
while i<=n:
    k=n-i
    j=1
    g=i
    p=(2*i)-2
    h=i
    while k>0:
        print(" ",end="")
        k-=1
    while j<=i:
        print(g,end="")
        g+=1
        j+=1
    while h>1:
        print(p,end="")
        h-=1
        p-=1
    print("")
    i+=1
    
