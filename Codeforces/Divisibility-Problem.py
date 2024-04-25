t=int(input())
for i in range(0,t):
    a,b=input().split()
    if int(a)%int(b) == 0:
        print("0")
    if int(a)%int(b) != 0:
        mod=int(a)%int(b)
        ans=int(b)-mod
        print(ans)