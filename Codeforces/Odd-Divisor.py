t=int(input())
for i in range(0, t):
    n=int(input())
    if n%2==1:
        print("YES")
    else:
        while n%2==0:
            n=n/2
        print("YES") if n>1 else print("NO")