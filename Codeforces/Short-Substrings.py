t=int(input())
for i in range(0, t):
    s=input()
    lst=[]
    for i in range(0, len(s)-1, 2):
        if s[i]!=s[i+1] or s[i]==s[i+1]:
            lst.append(s[i])
    lst.append(s[-1])
    print("".join(lst))