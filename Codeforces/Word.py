uppercase=0
lowercase=0
str=input()
for i in range(len(str)):
    x=ord(str[i])
    if x>=65 and x<=90:
        uppercase+=1
    else:
        lowercase+=1

if uppercase < lowercase:
    print(str.lower())
elif lowercase < uppercase:
    print(str.upper())
else:
    print(str.lower())