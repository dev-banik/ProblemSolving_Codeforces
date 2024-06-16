t = int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int, input().split())) 
    lst.sort()    
    possible=True    
    for i in range(1, n):
        if lst[i] - lst[i-1] > 1:
            possible=False
            break    
    print("YES") if possible else print("NO")