t=int(input())
for i in range(0, t):
    n=int(input())
    lst=list(map(int, input().split()))
    if lst[0]!=lst[1] and lst[1]==lst[2]:
        print("1")
    else:
        x=lst[0]
        for i in range(0, len(lst)):
            if lst[i]!=x:
                print(i+1)
                break