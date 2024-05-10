count = {}  
n = int(input())
for i in range(n):
    s = input()
    if s not in count:
        count[s] = 0  
        print("OK")
    else:
        count[s] += 1  
        print(s+str(count[s]))