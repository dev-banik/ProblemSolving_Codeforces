import itertools
t=int(input())
for i in range(0, t):
    k=int(input())
    for i in itertools.count(1):
        if (i%3==0) or (i%10==3):
            continue
        else:
            k-=1
            if k==0:
                print(i)
                break