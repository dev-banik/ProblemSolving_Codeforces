import bisect
n=int(input())
bottle_price=list(map(int, input().split()))
bottle_price.sort()
days = int(input())
for _ in range(days):
    coin = int(input())
    count = bisect.bisect_right(bottle_price, coin)
    print(count)