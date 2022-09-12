# using loops
n=5
factorial=1
if(n<0):
    print("no factorial")
elif(n==0):
    print("factorial is :",1)
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print(factorial)

#####################################################################################


# using recursion

def factor(x):
    if x==1:
        return 1
    else:
        return (x*factor(x-1))
print(factor(5))
