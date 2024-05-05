count=0
check=0
n=int(input())
a=input().split()
lst=list(a)
for i in range(0, n):
    if int(lst[i])>=int(lst[i-1]):
        count+=1
        if count>check:
            check=count
    else:
        count=1
print(check)