n,m=map(int, input().split())
lst=list(map(int, input().split()))
lst.sort()
last_value=lst[n-1]-lst[0]
for i in range(1, (m-n)+1):
    if (lst[i+n-1]-lst[i])<last_value:
        last_value=lst[i+n-1]-lst[i]
print(last_value)    