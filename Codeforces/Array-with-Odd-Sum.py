t=int(input())
for _ in range(0, t):
    even_count,odd_count=0,0
    n=int(input())
    lst=list(map(int, input().split()))
    for i in range(0, len(lst)):
        if lst[i]%2==0:
            even_count+=1
        else:
            odd_count+=1
    print("YES") if ((sum(lst)%2!=0) or (even_count and odd_count)) else print("NO") 