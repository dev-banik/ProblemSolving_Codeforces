n,k=map(int, input().split())
lst=[]
time=k
solve=0
for i in range(1, n+1):
    lst.append(i*5)
for i in range(0, len(lst)):
    time+=lst[i]
    if time>240:
        break
    solve+=1
print(solve)