count=0
n,k=input().split()
y=input().split()
lst=list(y)
for i in lst:
    if int(i)<5:
        if 5-int(i) >= int(k):
            count+=1
print(int(count/3)) if count>=3 else print("0")