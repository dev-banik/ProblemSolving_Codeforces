count=0
str=input()
for i in range(len(str)):
    if str[i] == '4' or str[i] == '7':
        count+=1
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")