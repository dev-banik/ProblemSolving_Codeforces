t=int(input())
for _ in range(0, t):
    n=int(input())
    lst=list(map(int, input().split()))
    print("YES") if (sum(lst)%2!=0) else print("NO")