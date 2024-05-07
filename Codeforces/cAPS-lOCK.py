upper=0
lower=0
s=input()
for i in s:
    if i.isupper():
        upper+=1
    else:
        lower+=1
if s[0].islower() and upper==len(s)-1:
    for i in range(0,len(s)):
        if i==0:
            print(s[i].capitalize(),end='')
        else:
            print(s[i].lower(),end='')
elif upper==len(s):
    for i in range(len(s)):
        print(s[i].lower(),end='')
else:
    print(s)