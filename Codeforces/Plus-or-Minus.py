t=int(input())
for i in range(0, t):
    a,b,c=input().split()
    print("+") if int(a)+int(b)==int(c) else print("-")