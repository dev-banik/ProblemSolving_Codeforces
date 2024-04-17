import math
count=0
n,h=input().split()
a=input().split()
for i in range(0, int(n)):
    if int(a[i])<=int(h):
        count+=1
    else:
        count+=math.ceil(int(a[i])/int(h))
print(count)