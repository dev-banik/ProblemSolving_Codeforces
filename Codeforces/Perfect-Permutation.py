n=int(input())
if n%2!=0:
    print(-1)
else:
    lst=[]
    for i in range(1,n+1,2):
        lst.append(i+1)
        lst.append(i)
    print(' '.join(map(str, lst)))