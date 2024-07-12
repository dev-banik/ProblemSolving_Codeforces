sum1,sum2,count=0,0,0
n=int(input())
lst=list(map(int, input().split()))
lst.sort(reverse=True)
sum1=sum(lst)/2
for i in range(0, n):
    sum2+=lst[i]
    count+=1
    if sum1<sum2:
        break
print(count)