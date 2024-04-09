i=0
count=0
input_take_lst=[]
lst=[]

input_takes_lst=input().split()
for input_val in input_takes_lst:
    a=int(input_val)
    input_take_lst.append(a)

inputs=input().split()
for val in inputs:
    b=int(val)
    lst.append(b)

for c in lst:
    if c != 0 and c>=lst[input_take_lst[1]-1]:
        count+=1

print(count)
count=0