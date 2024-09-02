n,m=map(int, input().split())
x=n+1
while True:
    is_prime = True
    if x<=1:
        is_prime = False
    elif x<=3:
        is_prime = True
    elif x % 2 == 0 or x % 3 == 0:
        is_prime = False
    else:
        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                is_prime = False
                break
            i += 6
    if is_prime:
        break
    x += 1
print("YES") if x==m else print("NO")
