t=int(input())
for i in range(0, t):
    s=input()
    if len(s)%2==0:
        if s[:len(s)//2]==s[len(s)//2:]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")