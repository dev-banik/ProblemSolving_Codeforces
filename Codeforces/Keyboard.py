res=[]
char="qwertyuiopasdfghjkl;zxcvbnm,./"
direction=input()
s=input()
if direction=="R":
    for i in range(0, len(s)):
        for j in range(0, len(char)):
            if s[i]==char[j]:
                res.append(char[j-1])
                break
if direction=="L":
    for i in range(0, len(s)):
        for j in range(0, len(char)):
            if s[i]==char[j]:
                res.append(char[j+1])
                break
print("".join(res))