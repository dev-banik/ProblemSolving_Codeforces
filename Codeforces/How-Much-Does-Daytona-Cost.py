t=int(input())
for _ in range(0, t):
    flag=False
    n,k=map(int, input().split())
    lst=list(map(int, input().split()))
    for i in range(0, len(lst)):
        if lst[i]==k:
            flag=True
            break
        else:
            flag=False
    print("YES") if flag else print("NO")