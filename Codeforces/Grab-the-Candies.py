t=int(input())
for _ in range(0, t):
    count_even,count_odd=0,0
    n=int(input())
    lst=list(map(int, input().split()))
    lst.sort(reverse=True)
    for i in range(0, len(lst)):
        if lst[i]%2==0:
            count_even+=lst[i]
        else:
            count_odd+=lst[i]
    print("YES") if count_even>count_odd else print("NO")