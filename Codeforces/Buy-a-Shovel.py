import itertools
sum=0
k,r=map(int, input().split())
for i in itertools.count():
    sum+=k
    if sum%10==0 or sum%10==r:
        print(i+1)
        break
    else:
        continue