count=0
n=int(input())
for i in range(n):
    pq=input().split()
    if abs(int(pq[0]) - int(pq[1])) >= 2:
        count+=1
print(count)