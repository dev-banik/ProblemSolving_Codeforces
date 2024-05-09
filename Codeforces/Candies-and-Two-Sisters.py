t=int(input())
for i in range(0,t):
    n=int(input())
    if n%2==0:
        print(int((n-1)/2))
    else:
        print(int(n/2))