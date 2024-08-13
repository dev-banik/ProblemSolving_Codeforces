t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    occupied = set()    
    valid = True    
    for i in range(n):
        if i > 0:  
            prev_occupied = occupied
            if not (a[i] - 1 in prev_occupied or a[i] + 1 in prev_occupied):
                valid = False
                break
        occupied.add(a[i])
    print("YES") if valid else print("NO")