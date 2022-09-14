n = 100
s =2

while s<=n:
    flag = False
    d=2
    while d<s:
        if s%d==0:
           flag = True
        d=d+1
    if not flag:
        print(s,end=" ")
    s=s+1
            
        
