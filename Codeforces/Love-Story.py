t=int(input())
for _ in range(0, t):
    s1='codeforces'
    count=0
    s=input()
    for i in range(0, len(s)):
        if s[i] != s1[i]:
            count+=1
    print(count)