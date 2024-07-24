t=int(input())
for _ in range(0, t):
    n=int(input())
    s=input()
    for i in range(0, len(s)):
        if s[i]=="B":
            begin=i
    for i in range(len(s)-1, -1, -1):
        if s[i]=="B":
            end=i
    print(abs(end-begin)+1)