t=int(input())
for _ in range(0, t):
    count=0
    n,m,k=map(int, input().split())
    lst_b=list(map(int, input().split()))
    lst_c=list(map(int, input().split()))
    for i in range(0, len(lst_b)):
        for j in range(0, len(lst_c)):
            if lst_b[i]+lst_c[j]<=k:
                count+=1
    print(count)