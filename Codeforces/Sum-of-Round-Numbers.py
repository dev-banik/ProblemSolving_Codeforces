lst=[]
t=int(input())
for i in range(0, t):
    n=int(input())
    if n%10!=0:
        lst.append(n%10)
        n-=n%10
    if n%100!=0:
        lst.append(n%100)
        n-=n%100
    if n%1000!=0:
        lst.append(n%1000)
        n-=n%1000
    if n%10000!=0:
        lst.append(n%10000)
    if n>=10000 and n%10000==0:
        lst.append(n)
    print(len(lst))    
    result = " ".join(map(str, lst))  
    print(result)
    lst=[]