t=int(input())
for _ in range(0, t):
    n=int(input())
    if n%3==0:
        ans1=int(n/3)
        ans2=int(n/3)
    elif n%3==1:
        ans1=int(n/3)+1
        ans2=int(n/3)
    elif n%3==2:
        ans1=int(n/3)
        ans2=int(n/3)+1
    print(ans1, ans2)