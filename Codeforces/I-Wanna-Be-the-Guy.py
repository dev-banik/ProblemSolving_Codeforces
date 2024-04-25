lst = []
n = int(input())
lil_x = input().split()[1:] 
lil_y = input().split()[1:] 
lst.extend(lil_x)
lst.extend(lil_y)
lst=list(set(lst))
lst.sort()
if n==len(lst):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")