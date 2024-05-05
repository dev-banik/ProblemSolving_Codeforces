n = int(input())
lst = [100, 20, 10, 5, 1]
res = 0
for i in lst:
    bills = n // i
    res += bills
    n -= bills * i
print(res)