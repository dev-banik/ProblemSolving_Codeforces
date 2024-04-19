count=0
lst=[]
n=int(input())
ab=input().split()
lst=list(ab)
for i in lst:
    if i == '1':
        print("HARD")
        count+=1
        break
if count==0:
    print("EASY")