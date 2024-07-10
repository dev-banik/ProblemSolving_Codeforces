import math
n = int(input())
lst = list(map(int, input().split()))

limit = int(math.isqrt(10**12)) + 1
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False 
p = 2
while p * p <= limit:
    if is_prime[p]:
        for i in range(p * p, limit + 1, p):
            is_prime[i] = False
    p += 1

for num in lst:
    if num == 1:
        print("NO")
        continue
    sqrt_num = int(math.isqrt(num))
    if sqrt_num * sqrt_num == num and is_prime[sqrt_num]:
        print("YES")
    else:
        print("NO")