b=6
y,w=map(int, input().split())
a=7-max(y,w)
for i in range(2, 7):
    if a%i==0 and b%i==0:
        a/=i
        b/=i
print(f"{int(a)}/{int(b)}")