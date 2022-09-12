def gcd_fun (x, y):  
    if (y == 0): # it divide every number  
        return x  # return x  
    else:  
        return gcd_fun (y, x % y)  

print(gcd_fun(24,54))
