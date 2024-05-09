even=0
odd=0
n=int(input())
num=input().split()
lst=list(num)
for i in range(0,len(lst)):
    if int(lst[i])%2==0:
        even+=1
        diff_even=i
    else:
        odd+=1
        diff_odd=i
if odd<even:
    print(diff_odd+1)
else:
    print(diff_even+1)    