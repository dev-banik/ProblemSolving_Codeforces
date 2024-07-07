lst_pr,lst_m,lst_pe=[],[],[]
n=int(input())
lst=list(map(int, input().split()))
for i in range(0, len(lst)):
    if lst[i]==1:
        lst_pr.append(i)
    elif lst[i]==2:
        lst_m.append(i)
    elif lst[i]==3:
        lst_pe.append(i)
max_team=min(len(lst_pr),len(lst_m),len(lst_pe))
print(max_team)
for i in range(0, max_team):
    print(lst_pr[i]+1,lst_m[i]+1, lst_pe[i]+1)