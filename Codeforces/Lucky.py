t=int(input())
for i in range(0, t):
    s=input()
    print("YES") if (int(s[0])+int(s[1])+int(s[2])) == (int(s[3])+int(s[4])+int(s[5])) else print("NO")