t=int(input())
for _ in range(0, t):
    n=int(input())
    if n%2==0:
        print(int(n/2))
    else:
        print(int((n+1)/2))