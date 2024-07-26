t = int(input()) 
for _ in range(t):
    n, k = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    reduced_grid = []
    for i in range(0, n, k):
        reduced_row = ""
        for j in range(0, n, k):
            block_value = grid[i][j]
            reduced_row += block_value
        reduced_grid.append(reduced_row)
    for row in reduced_grid:
        print(row)