n=int(input())
i=n
while i>0:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print("")
    i-=1
# ans:- 
# 4
# ****
# ***
# **
# *

#################################################################

n=int(input())
i=1
while i<=n:
    j=1
    k=n-i
    if k>0:
        while k>0:
            print(" ",end="")
            k-=1
    while j<=i:
        print("*",end="")
        j+=1
    print("")
    i+=1

# ans:-
# 10
#          *
#         **
#       ***
#       ****
#      *****
#     ******
#   *******
#   ********
#  *********
# **********

#################################################################################

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
        print(j,end="")
        j+=1
    while p<=i and p!=0:
        print(p,end="")
        p-=1
    print("")
    i+=1
# ans:-
# 4
#   1
#   121
#  12321
# 1234321
