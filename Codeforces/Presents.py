n = int(input())
p = input().split()

ans = ''
for i in range(1, n+1):
    for j in range(0, n):
        if int(p[j]) == int(i):
            ans += str(j+1) + ' '

print(ans)