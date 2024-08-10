t=int(input())
for _ in range(0, t):
    x, y, k = map(int, input().split())
    v = []
    if k % 2 == 1:
        v.append((x, y))
    for i in range(1, k // 2 + 1):
        v.append((x - i, y - i))
    for i in range(1, k // 2 + 1):
        v.append((x + i, y + i))
    for it in v:
        print(it[0], it[1])