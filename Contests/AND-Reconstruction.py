t=int(input())
for _ in range(0, t):
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    for i in range(n - 1):
        a[i] |= b[i]
        a[i + 1] |= b[i]
    for i in range(n - 1):
        if b[i] != (a[i] & a[i + 1]):
            print(-1)
            break
    else:
        print(" ".join(map(str, a)))