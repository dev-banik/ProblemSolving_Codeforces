y=int(input())
for i in range(y, 10000):
    i+=1
    a=int(i/1000)
    b=int(i/100)%10
    c=int(i/10)%10
    d=int(i%10)
    if(a!=b and a!=c and a!=d and b!=c and b!=d and c!=d):
        print(i)
        break