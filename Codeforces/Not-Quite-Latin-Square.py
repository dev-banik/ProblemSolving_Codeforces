t=int(input())
for _ in range(0, t*3):
    A,B,C=0,0,0
    s=input()
    for i in range(0, len(s)):
        if s[i]=="A":A+=1
        if s[i]=="B":B+=1
        if s[i]=="C":C+=1
    if A==0:print("A")
    if B==0:print("B")
    if C==0:print("C")