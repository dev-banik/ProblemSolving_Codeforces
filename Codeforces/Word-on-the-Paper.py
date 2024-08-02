t=int(input())
for _ in range(0, t):
    res=[]
    for i in range(0, 8):
        s=input()
        for j in range(0, len(s)):
                if s[j] != ".":
                    res.append(s[j])
    print(''.join(res))