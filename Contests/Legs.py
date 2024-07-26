t = int(input())
for _ in range(t):
    n = int(input())  
    cows = n // 4
    remaining_legs = n % 4
    if remaining_legs == 0:
        min_animals = cows
    else:
        min_animals = cows + 1 
    print(min_animals)