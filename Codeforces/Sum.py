t=int(input())
for i in range(0, t):
    a,b,c=map(int, input().split())
    print("YES") if (a+b)==c or (b+c)==a or (a+c)==b else print("NO")