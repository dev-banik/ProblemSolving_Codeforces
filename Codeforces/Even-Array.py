t=int(input())
for _ in range(0, t):
    lst=[]
    even_number,odd_number,fine_number=0,0,0
    n=int(input())
    lst=list(map(int, input().split()))
    for i in range(0, n):
        if i%2==0:
            if lst[i]%2==0:
                fine_number+=1
            else:
                odd_number+=1
        else:
            if lst[i]%2!=0:
                fine_number+=1
            else:
                even_number+=1
    if fine_number==n:
        print(0)
    elif even_number==odd_number:
        print(even_number)
    else:
        print("-1")