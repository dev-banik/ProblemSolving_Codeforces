sum_x=0
sum_y=0
sum_z=0

n=int(input())
for i in range(n):
    x,y,z=input().split()
    sum_x+=int(x)
    sum_y+=int(y)
    sum_z+=int(z)

if sum_x==0 and sum_y==0 and sum_z==0:
    print("YES")
else:
    print("NO")
