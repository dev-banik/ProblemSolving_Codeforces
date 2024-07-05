crime_count,police_count=0,0
n=int(input())
lst=list(map(int, input().split()))
for i in range(0, len(lst)):
    if lst[i]>0:
        police_count+=lst[i]
    else:
        if police_count<1:
            crime_count+=1
        else:
            police_count-=1
print(crime_count)