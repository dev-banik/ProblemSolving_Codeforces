x_string=[]
y_string=[]
has_value=0

x=input()
y=input()

for val in x:
    a=ord(val.lower())
    x_string.append(a)

for val in y:
    b=ord(val.lower())
    y_string.append(b)

for val_x in range(len(x_string)):
    if x_string[val_x] > y_string[val_x]:
        has_value=1
        break

    elif x_string[val_x] < y_string[val_x]:
        has_value=-1
        break

    else:
        continue

if has_value != 0:
    print(has_value)
else:
    print(has_value)