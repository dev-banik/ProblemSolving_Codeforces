t = int(input())
for i in range(t):
    s = input()
    if len(set(s)) == 1:
        print("NO")
    else:
        print("YES")
        sort_c = sorted(s)
        if sort_c == list(s):
            print("".join(sort_c[::-1]))
        else:
            print(''.join(sort_c))