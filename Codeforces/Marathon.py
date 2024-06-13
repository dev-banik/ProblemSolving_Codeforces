t=int(input())
for i in range(0, t):
    count=0
    a,b,c,d=map(int, input().split())
    if a<b:
        count+=1
    if a<c:
        count+=1
    if a<d:
        count+=1
    print(count)