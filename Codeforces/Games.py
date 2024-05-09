count=0
n=int(input())
h_lst=[]
g_lst=[]
for i in range(0,n):
    h_uni,g_uni=input().split()
    h_lst.append(h_uni)
    g_lst.append(g_uni)
for i in range(0, n):
    for j in range(0, n):
        if int(h_lst[i])==int(g_lst[j]):
            count+=1
print(count)