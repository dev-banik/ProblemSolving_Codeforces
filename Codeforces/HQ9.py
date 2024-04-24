count=0
str=input()
for i in range(0, len(str)):
    if str[i] == 'H' or str[i] == 'Q' or str[i] == '9':
        print("YES")
        count+=1
        break
if count==0:
    print("NO")