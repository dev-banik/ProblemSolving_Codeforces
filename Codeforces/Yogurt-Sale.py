t=int(input())
for _ in range(0, t):
    n,a,b=map(int, input().split())
    print(n*a) if (2*a)<b else print(int(n/2)*b+(n%2)*a)       