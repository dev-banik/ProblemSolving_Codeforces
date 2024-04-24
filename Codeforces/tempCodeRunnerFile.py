count=0
a=input().split()
lst=list(a)
for i in range(0, len(lst)):
    for j in range(i+1, len(lst)):
        if a[i] == a[j]:
            lst.remove(a[j])
            count+=1
print(count)