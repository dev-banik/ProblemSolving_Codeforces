char="abcdefghijklmnopqrstuvwxyz"
count,init_pos=0,'a'
s=input()
for i in range(0, len(s)):
    count+=min(abs(ord(init_pos)-ord(s[i])), 26-abs(ord(s[i])-ord(init_pos)))
    init_pos=s[i]
print(count)