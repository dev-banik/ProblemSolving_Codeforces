t=int(input())
for _ in range(0,t):
    max_value=-1
    n=int(input())
    lst=list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        max_value=max(max_value, lst[i])
    print(max_value)