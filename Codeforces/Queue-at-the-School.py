n, t = input().split()
s = input()
s_lst = list(s)  
for i in range(int(t)):
    j = 0
    while j < len(s) - 1:
        if s_lst[j] == 'B' and s_lst[j+1] == 'G':
            s_lst[j], s_lst[j+1] = s_lst[j+1], s_lst[j]
            j += 1  
        j += 1  
s = ''.join(s_lst)  
print(s)