count=0
x=int(input())
while x>0:
    if x%2==1:
        count+=1
    x//=2
print(count)