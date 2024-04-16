n,k=input().split()
for i in range(int(k)):
    n=int(n)
    if int(n)%10==0:        
        n/=10
    else:
        n-=1

print(int(n))