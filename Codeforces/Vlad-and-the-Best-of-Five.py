t=int(input())
for _ in range(0, t):
    count_a,count_b=0,0
    s=input()
    for i in range(0, len(s)):
        if s[i]=="A": count_a+=1
        elif s[i]=="B": count_b+=1
    print("A") if count_a>count_b else print("B")