import math
n,k=input().split()
if int(n)%2==0:
    a=int(n)/2
else:
    a=math.ceil(int(n)/2)

if a>=int(k):
    print(int((int(k)*2)-1))
else:
    print(int((int(k)-a)*2))