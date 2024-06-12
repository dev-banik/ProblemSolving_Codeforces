import math
t=int(input())
for i in range(0, t):
    x1,y1=map(int, input().split())
    x2,y2=map(int, input().split())
    x3,y3=map(int, input().split())
    x4,y4=map(int, input().split())
    if x1==x3 and x2==x4:
        area=math.sqrt((x1-x3)**2+(y1-y3)**2)
        ans=area**2
    else:
        x1_value=abs(x1-x3)
        x2_value=abs(x2-x4)
        ans=x1_value*x2_value        
    print(int(ans))
    ans=0