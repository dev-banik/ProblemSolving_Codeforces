t=int(input())
for i in range(0, t):
    a,b,c=map(int, input().split())
    if a==b and a!=c:
        print(c)
    elif a!=b and a==c:
        print(b)
    else:
        print(a)