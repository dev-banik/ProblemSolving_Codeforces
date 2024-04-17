count=0
is_dengerous=0

str=input()
for i in range(len(str)-1):
    # print("str[i]= {} and str[i+1]= {}", str[i], str[i+1])
    if str[i] == str[i+1]:
        count+=1
        # print("count is=",count)
        if count>=6:
            is_dengerous+=1
            print("YES")
            break
    else:
        count=0
if is_dengerous==0:
    print("NO")
