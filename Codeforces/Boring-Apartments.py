t=int(input())
for _ in range(0, t):
    flag=False
    count=0
    x=int(input())
    for i in range(1, 10):
        for j in range(1, 5):
            count+=len(str(str(i)*j))
            if str(str(i)*j)==str(x):
                flag=True
                break
        if flag:
            break
        else:
            continue 
    print(count)