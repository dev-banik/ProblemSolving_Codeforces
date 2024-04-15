sum=0

k,n,w=input().split()
for i in range(int(w)+1):
    sum=sum+i

ans=(int(sum)*int(k))-int(n)
if ans<0:
    print("0")
else:
    print(ans)
