sum=0
n=int(input())
p=input().split()
for i in range(len(p)):
    sum+=int(p[i])   
print("{:.12f}".format(sum / n))