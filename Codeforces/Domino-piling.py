lst=[]
mul_result=1
result=0

mn=input().split()
for val in mn:
    a=int(val)
    lst.append(a)

for b in lst:
    mul_result=mul_result * b

result=int(mul_result/2)
print(result)