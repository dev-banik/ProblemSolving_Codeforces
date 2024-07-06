s,n=map(int, input().split())
strength=s
flag=False
lst=[]  
for i in range(0, n):
    x,y=map(int, input().split())
    lst.append((x,y))
lst.sort(key=lambda pair: pair[0])
for x,y in lst:
    if strength>x:
        strength+=y
    else:
        print("NO")
        flag=True
        break
if flag==False:
    print("YES")