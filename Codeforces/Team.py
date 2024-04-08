count = 0
counta = 0
lst = []
n = int(input())
for i in range(n):
    inputs = input().split()  
    for val in inputs:
        b = int(val)  
        lst.append(b)

    for a in lst:
        if a == 1:
            counta+=1

    if counta>=2:
        count+=1

    lst = [] 
    counta=0 

print(count)
count=0