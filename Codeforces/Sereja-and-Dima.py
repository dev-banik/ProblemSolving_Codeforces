n=int(input())
lst=list(map(int, input().split()))

s_score,d_score=0,0
left,right=0,n-1
turns="sereja"

for _ in range(0, n):
    if turns=="sereja":
        if lst[left]>lst[right]:
            s_score+=lst[left]
            left+=1
        else:
            s_score+=lst[right]
            right-=1
        turns="dima"
    else:
        if lst[left]>lst[right]:
            d_score+=lst[left]
            left+=1
        else:
            d_score+=lst[right]
            right-=1
        turns="sereja"
print(s_score, d_score)
