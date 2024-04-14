n=int(input())
str=input()

count=0
for i in range(len(str)):
    for j in range(i+1, len(str)):
        if str[i]==str[j]:
            count+=1
        break

print(count)
