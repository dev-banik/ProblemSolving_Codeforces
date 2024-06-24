t=int(input())
for i in range(0, t):
    a,b,c=map(int, input().split())
    print("YES") if (a+b>=10) or (a+c>=10) or (b+c>=10) else print("NO")