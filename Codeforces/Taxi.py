import math
count_a,count_b,count_c,count_d,count_texi=0,0,0,0,0
n=int(input())
lst=list(map(int, input().split()))
for i in range(0, len(lst)):
    if lst[i]==1:
        count_a+=1
    elif lst[i]==2:
        count_b+=1
    elif lst[i]==3:
        count_c+=1
    elif lst[i]==4:
        count_d+=1
count_texi+=count_d #group-4
count_texi+=count_c #group-3
count_a-=count_c
if count_a<0:
    count_a=0
if count_b%2==0:    #group-2
    count_b=int(count_b/2)
    count_texi+=count_b
else:
    count_b=int(count_b/2)+1
    count_texi+=count_b
    count_a-=2
    if count_a<0:
        count_a=0
count_a=math.ceil(count_a/4) #group-1
count_texi+=int(count_a)
print(math.ceil(count_texi))