# Code : Character Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# A
# BC
# CDE
# DEFG
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 13
# Sample Input 1:
# 5
# Sample Output 1:
# A
# BC
# CDE
# DEFG
# EFGHI
# Sample Input 2:
# 6
# Sample Output 2:
# A
# BC
# CDE
# DEFG
# EFGHI
# FGHIJK

n=int(input())
i=1
abc="A"
asci=ord(abc)
while i<=n:
    j=1
    k=asci
    while j<=i:
        print(chr(k),end="")
        j+=1
        k+=1
    asci+=1
    print("")
    i+=1
