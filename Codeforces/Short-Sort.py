a="abc"
lst_a=list(a)
t=int(input())
for i in range(0, t):
    count=0
    s=input()
    if s=="abc":
        print("YES")
    else:
        lst=list(s)
        for i in range(0, 3):
            if lst[i]!=lst_a[i]:
                count+=1
            else:
                continue
        print("YES") if count==0 or count==2 else print("NO")    