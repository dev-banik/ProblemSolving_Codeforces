sum=0
n=int(input())
lst=list(map(int, input().split())) 
lst.sort()
for i in range(0, len(lst)-1):
    sum+=int(lst[n-1]) - int(lst[i])
print(sum)