ans=0
a,b,c,d=map(int, input().split())
s=input()
for i in range(0, len(s)):
    if s[i]=="1":
        ans+=a 
    elif s[i]=="2":
        ans+=b
    elif s[i]=="3":
        ans+=c
    elif s[i]=="4":
        ans+=d
print(ans)