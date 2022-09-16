n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print("",j,end="")
        j=j+1
    print("")
    i=i+1
# ans :-
# 4
#  1
#  1 2
#  1 2 3
#  1 2 3 4

#######################################

n=4
i=1
while i<=n:
    k=i
    j=1
    while j<=i:
        print("",k,end="")
        j+=1
        k+=1
    print("")
    i+=1
# ans:-
#  1
#  2 3
#  3 4 5
#  4 5 6 7

########################################
n=int(input())
i=1
k=1
while i<=n:
    j=1
    while j<=i:
        print(k,end=" ")
        k=k+1
        j=j+1
    print("")
    i=i+1
# ans :-
# 4
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

        
