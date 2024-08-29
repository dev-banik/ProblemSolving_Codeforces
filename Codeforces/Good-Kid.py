t=int(input())
for _ in range(0 ,t):
    mul = 1
    n=int(input())
    lst=list(map(int, input().split()))
    lst.sort()
    lst[0] = lst[0] + 1
    for i in lst:
        mul *= i
    print(mul)