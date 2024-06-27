t=int(input())
for i in range(0, t):
    lst_even=[]
    lst_odd=[]
    lst_even_sum=0
    lst_odd_sum=0
    n=int(input())
    if n%2==0 and n%4==0:
        print("YES")
        for i in range(1, n+1):
            if i%2==0:
                lst_even.append(i)
                lst_even_sum+=i
            else:
                lst_odd.append(i)
                lst_odd_sum+=i
        if lst_odd_sum==lst_even_sum:
            combine_lst=lst_even+lst_odd
            print(" ".join(map(str, combine_lst)))
        else:
            remain=lst_odd[-1]+(lst_even_sum-lst_odd_sum)
            lst_odd[-1]=remain
            combine_lst=lst_even+lst_odd
            print(" ".join(map(str, combine_lst)))
    else:
        print("NO")