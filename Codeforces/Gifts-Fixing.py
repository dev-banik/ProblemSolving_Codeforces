t=int(input())
for _ in range(0, t):
    lst_candy,lst_orange,count=[],[],0
    n=int(input())
    lst_candy=list(map(int, input().split()))
    lst_orange=list(map(int, input().split()))
    lst_candy_min=min(lst_candy)
    lst_orange_min=min(lst_orange)
    for i in range(0, n):
        count+=max((lst_candy[i]-lst_candy_min),(lst_orange[i]-lst_orange_min))
    print(count)