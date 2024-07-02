t=int(input())
for _ in range(0 ,t):
    lst=[]
    flag=False
    n=int(input())
    s=input()    
    for i in range(0, len(s)-1):
        if s[i]!=s[i+1]:
            if s[i+1] not in lst:
                lst.append(s[i])
            else:
                flag=True
                break
    print("NO") if flag else print("YES")