t=int(input())
for _ in range(0, t):
    lst_ans=[]
    n=int(input())
    lst=list(map(int, input().split()))
    lst.sort()
    for i in range(0, len(lst)-1):
        lst_ans.append(abs(lst[i]-lst[i+1]))
    print(min(lst_ans))