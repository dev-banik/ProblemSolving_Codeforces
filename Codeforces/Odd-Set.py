t=int(input())
for _ in range(0, t):
    lst_sum,lst_even,lst_odd=[],0,0
    n=int(input())
    lst=list(map(int, input().split()))
    for i in range(0, len(lst)):
        if lst[i]%2==0:
            lst_even+=1
        else:
            lst_odd+=1
    print("YES") if lst_even==lst_odd else print("NO")