n=int(input())
for _ in range(0, n):
    x,y=map(int, input().split())
    print("YES") if y>=-1 else print("NO")