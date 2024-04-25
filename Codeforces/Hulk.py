n = int(input())
ans = []
for i in range(1, n):
    if i % 2 == 0:
        ans.append("I love that")
    else:
        ans.append("I hate that")
if n % 2 == 0:
    ans.append("I love it")
else:
    ans.append("I hate it")
print(' '.join(ans))