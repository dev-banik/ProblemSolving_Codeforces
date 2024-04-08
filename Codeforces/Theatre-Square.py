import math

lst=[]
val=input().split()
for i in val:
    a=int(i)
    lst.append(a)
resa = math.ceil(lst[0]/lst[2])
resb = math.ceil(lst[1]/lst[2])
res = resa*resb
print(res)