# n =int(input())
n=4
i=1
abc="A"

while i<=n:
    j=1
    asci = ord(abc)
    while j<=n:
        print(chr(asci),end="")
        asci+=1
        j+=1
    print("")
    i+=1
    
# #   ans:- 
   
# # ABCD
# # ABCD
# # ABCD
# # ABCD

n=4
i=1
abc="A"
asci=ord(abc)
while i<=n:
    j=1
    k=asci
    while j<=n:
        print(chr(k),end="")
        k+=1
        j+=1
    asci+=1
    print("")
    i+=1
# ans:-
# ABCD
# BCDE
# CDEF
# DEFG
