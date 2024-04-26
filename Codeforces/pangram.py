n = int(input())
s = input().lower()  
u = set(s)
if len(u) == 26:
    print("YES")
else:
    print("NO")