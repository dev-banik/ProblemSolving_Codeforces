t=int(input())
for i in range(0, t):
    lst=list(map(int, input().split()))
    lst.sort()
    print(lst[1])