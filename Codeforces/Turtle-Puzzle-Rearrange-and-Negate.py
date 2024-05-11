ans=0
t=int(input())
for i in range(0, t):
    n=int(input())
    a=input().split()
    lst=list(a)
    for i in lst:
        ans+=abs(int(i))
    print(ans)
    ans=0