earn,count=0,0
m,n=map(int, input().split())
lst=list(map(int, input().split()))
lst.sort()
for i in range(0, len(lst)):
    if lst[i]<0:
        earn+=lst[i]
        count+=1
        if count==n:
            break
print(abs(earn))