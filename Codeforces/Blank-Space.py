t=int(input())
for _ in range(0, t):
    lst,lst_zero,count_zero=[],[],0
    n=int(input())
    lst=list(map(int, input().split()))
    for i in range(0, len(lst)):
        if lst[i]==0:
            count_zero+=1
            lst_zero.append(count_zero)
        elif lst[i]==1:
            lst_zero.append(count_zero)
            count_zero=0
    max_value=max(lst_zero)
    print(max_value)