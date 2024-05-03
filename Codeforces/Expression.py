max=0
a=int(input())
b=int(input())
c=int(input())
d=a+b*c
e=a*(b+c)
f=a*b*c
g=(a+b)*c
h=a+b+c
if d>max:
    max=d
if e>max:
    max=e
if f>max:
    max=f
if g>max:
    max=g
if h>max:
    max=h
print(max)