t=int(input())
for _ in range(0, t):
    n,x=map(int, input().split())
    if n<=2: print("1")
    else:
        n-=2
        print(int((n+x-1)/x+1))