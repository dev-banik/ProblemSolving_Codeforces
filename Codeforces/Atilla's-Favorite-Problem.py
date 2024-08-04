t=int(input())
for _ in range(0, t):
    s_value,count=0,0
    n=int(input())
    s=str(input())
    s=sorted(s)
    s_value=(ord(s[n-1]))
    count=(122-s_value)
    print((26-count))