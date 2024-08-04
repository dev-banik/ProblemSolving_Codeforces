t=int(input())
for _ in range(0, t):
    U,D,L,R,flag=0,0,0,0,False
    n=int(input())
    s=input()
    x_axis,y_axis=0,0
    for i in range(0, len(s)):
        if s[i]=="U":
            y_axis+=1
        elif s[i]=="D":
            y_axis-=1
        elif s[i]=="L":
            x_axis-=1
        elif s[i]=="R":
            x_axis+=1
        if x_axis==1 and y_axis==1:
            flag=True
            break
    print("YES") if flag==True else print("NO")