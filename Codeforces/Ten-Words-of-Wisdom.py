t=int(input())
for _ in range(0, t):
    max_count,win_count=-1,-1
    n=int(input())
    for i in range(1, n+1):
        a,b=map(int, input().split())
        if a<=10:
            if b>max_count:
                max_count=b
                win_count=i
    print(win_count)