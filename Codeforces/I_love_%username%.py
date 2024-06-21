n = int(input())
points = list(map(int, input().split()))
highest = points[0]
lowest = points[0]
amazing_count = 0
for i in range(1, n):
    if points[i] > highest:
        highest = points[i]
        amazing_count += 1
    elif points[i] < lowest:
        lowest = points[i]
        amazing_count += 1
print(amazing_count)