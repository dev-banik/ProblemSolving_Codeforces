n = int(input())
if n >= 0:
    print(n)
else:
    n = str(n)
    lst1 = list(n)
    lst2 = list(n)
    lst1.pop(-1)  
    lst2.pop(-2)  
    a = "".join(lst1)
    b = "".join(lst2)
    print(max(int(a), int(b)))