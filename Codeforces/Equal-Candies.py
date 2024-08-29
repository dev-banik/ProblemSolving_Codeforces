t=int(input())
for _ in range(0, t):
    ans=0
    n=int(input())
    lst=list(map(int, input().split()))
    lst.sort()
    min_value = min(lst)
    for i in lst:
        ans += (i-min_value)
    print(ans)