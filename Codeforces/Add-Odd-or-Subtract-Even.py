t=int(input())
for _ in range(0, t):
    a,b=map(int, input().split())
    if a==b:
        print(0)
    elif a>b:
        diff=a-b
        print(1) if diff%2==0 else print(2)
    elif a<b:
        diff=b-a
        print(1) if diff%2!=0 else print(2)