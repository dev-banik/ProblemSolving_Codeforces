t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 0:
        print(0)
        continue
    lengths = []
    for i in range(1, n + 1):
        lengths.append(i) 
    for i in range(n - 1, 0, -1):
        lengths.append(i) 
    lengths.sort(reverse=True)
    diagonals_used = 0
    for length in lengths:
        if k <= 0:
            break
        k -= min(k, length)
        diagonals_used += 1
    print(diagonals_used)