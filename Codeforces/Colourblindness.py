t=int(input())
for _ in range(0, t):
    flag=False
    n=int(input())
    s1=input()
    s2=input()
    for i in range(0, len(s1)):
        if (s1[i] != s2[i] and (s1[i] == 'R' or s2[i] == 'R')):
            flag=True
            break
        else:
            flag=False 
    print("NO") if flag else print("YES")