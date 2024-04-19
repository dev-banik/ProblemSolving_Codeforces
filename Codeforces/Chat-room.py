s=input()
a="hello"
j=0
count=0
for i in range(0, len(s)):
    if s[i] == a[j]:
        j+=1
        if j==5:
            print("YES")
            count+=1
            break

if count==0:
    print("NO")