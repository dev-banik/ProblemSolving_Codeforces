t=int(input())
for _ in range(t):
    w,h,n=map(int, input().split())
    pieces_count=1  
    while w%2==0:
        w//=2
        pieces_count*=2
    while h%2==0:
        h//=2
        pieces_count*=2
    print("YES") if pieces_count>=n else print("NO")