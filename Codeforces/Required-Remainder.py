import math
t=int(input())
for i in range(0, t):
    x,y,z=map(int, input().split())
    a=z-y
    b=math.floor(a/x)
    print(b*x+y)