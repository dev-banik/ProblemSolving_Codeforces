count=0
n=int(input())
for i in range(1, int(n/2)+1):
    if n%i==0:
        count+=1
print(count)