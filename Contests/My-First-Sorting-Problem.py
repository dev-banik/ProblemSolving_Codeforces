t=int(input())
for i in range(0,t):
    x,y=input().split()
    if int(x)<=int(y):
        print(x,y)
    else:
        print(y,x)