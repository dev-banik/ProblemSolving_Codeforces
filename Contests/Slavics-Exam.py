t = int(input())
for _ in range(t):
    s = list(input().strip())
    t_str = input().strip()
    t_len = len(t_str)
    s_len = len(s)    
    i, j = 0, 0
    while i < s_len and j < t_len:
        if s[i] == t_str[j]:
            j += 1
        elif s[i] == '?':
            s[i] = t_str[j]
            j += 1
        i += 1    
    if j < t_len:
        print("NO")
    else:
        s = ['a' if c == '?' else c for c in s]
        print("YES")
        print("".join(s))