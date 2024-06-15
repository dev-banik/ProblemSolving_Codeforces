lst=list(map(int, input().split()))
lst.sort()
last_number=int(''.join(map(str, lst[-1:])))
for i in range(0 ,len(lst)-1):
    print(last_number-lst[i], end=" ")