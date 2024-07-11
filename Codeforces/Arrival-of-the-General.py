max_value,min_value,max_count,min_count=0,101,0,0
n=int(input())
lst=list(map(int, input().split()))
for i in range(0, n):
    if lst[i]>max_value:
        max_value=lst[i]
        max_count=i
    if lst[i]<=min_value:
        min_value=lst[i]
        min_count=i
if max_count>min_count:
    min_count+=1
print(max_count+(n-1)-min_count)