t=int(input())
for i in range(0, t):
    count=0
    n=int(input())
    lst=list(map(int, input().split()))
    lst.sort()
    for i in range(0, n-1):
        a=lst[i+1]-lst[i]
        count+=a
    print(count)        