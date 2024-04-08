i=0
count=0
n=int(input())
while i<n:
    s=input()
    if(s=='++X' or s=='X++'):
        count+=1
    elif(s=='--X' or s=='X--'):
        count-=1
    else:
        count=0        
    i+=1
print(count)
