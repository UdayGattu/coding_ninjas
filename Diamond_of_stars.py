# Code : Diamond of stars
# Send Feedback
# Print the following pattern for the given number of rows.
# Note: N is always odd.


# Pattern for N = 5



# The dots represent spaces.



# Input format :
# N (Total no. of rows and can only be odd)
# Output format :
# Pattern in N lines
# Constraints :
# 1 <= N <= 49
# Sample Input 1:
# 5
# Sample Output 1:
#   *
#  ***
# *****
#  ***
#   *
# Sample Input 2:
# 3
# Sample Output 2:
#   *
#  ***
#   *
  
  
#  n =int(input())
# if n%2!=0:
#     f1 = (n+1)//2
#     s1 = n//2
#     i=1
#     while i<=f1:
#         j=1
#         h=2*i-1
#         k=f1-i
#         while k>0:
#             print(" ",end="")
#             k-=1
#         while j<=h:
#             print("*",end="")
#             j+=1
#         print("")
#         i+=1
 
  
  
n=int(input())
even = n%2==0

for i in range(1, n+1, 2):
    print(('*'*i).center(n))

for i in range(n-2-even, 0, -2):
    print(('*'*i).center(n))
