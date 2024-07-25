t=int(input())
for _ in range(0, t):
    count, flag=0, False
    n=int(input())
    lst=list(map(int, input().split()))
    lst.sort(reverse=True)
    for i in range(0, len(lst)-1):
        if lst[i]==lst[i+1]:
            count+=1
            if count==2:
                value=lst[i]
                flag=True
                break
        else:
            count=0
    print(value) if flag else print("-1")