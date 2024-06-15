count, current_stage=0,0
n,m=map(int, input().split())
lst=list(map(int, input().split()))
for i in lst:
    if i<current_stage:
        count+=n-abs(i-current_stage)
    else:
        count+=abs(i-current_stage)
    current_stage=i
print(count-1)