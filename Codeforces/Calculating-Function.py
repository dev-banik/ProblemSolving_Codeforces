import math
n=int(input())
if n%2==0:
    print(int(n/2))
else:
    print(int((-1)*math.ceil(n/2)))