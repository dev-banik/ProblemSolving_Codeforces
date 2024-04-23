lst=[]
a=input()
b=input()
for i in range(0, len(a)):
    for j in range(i, len(b)):
        if (a[i] == '1' and b[j] == '0'):
            ans='1'
            lst.append(ans)  
        elif (a[i] == '0' and b[j] == '1'):
            ans='1'
            lst.append(ans)
        elif (a[i] == '1' and b[j] == '1'):
            ans='0'
            lst.append(ans)   
        elif (a[i] == '0' and b[j] == '0'):
            ans='0'
            lst.append(ans)           
        break

ans=''.join(map(str, lst))
print(ans)
        

