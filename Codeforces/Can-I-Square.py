import math
t=int(input())
for i in range(0, t):
    n=int(input())
    lst=map(int, input().split())
    lst_sum=sum(lst)
    sqrt=math.sqrt(lst_sum)
    print("YES") if int(sqrt)**2==lst_sum else print("NO")