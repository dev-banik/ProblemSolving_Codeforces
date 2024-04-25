n = int(input())
s = input().split()
lst = [int(x) for x in s]  
lst.sort()
print(' '.join(map(str, lst)) )