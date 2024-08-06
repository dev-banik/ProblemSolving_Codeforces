t = int(input())
for _ in range(t):
    lst_count = []
    n = int(input())
    lst = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        count = lst[i].count(1)
        if count != 0:
            lst_count.append(count)
    lst_count = set(lst_count)
    print("SQUARE") if len(lst_count)==1 else print("TRIANGLE")