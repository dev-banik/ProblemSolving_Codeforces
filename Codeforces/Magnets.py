n=int(input())
n_pole=""
s_pole=""
count=0
for i in range(0, n):
    n_pole=int(input())
    if n_pole != s_pole:
        count+=1
        s_pole=n_pole
print(count)