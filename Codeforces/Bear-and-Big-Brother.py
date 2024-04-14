lst=[]
mn=input().split()
for val in mn:
    a=int(val)
    lst.append(a)

l=lst[0]
b=lst[1]

for i in range(1000):
    l *= 3
    b *= 2
    if l>b:
        print(i+1)
        break 