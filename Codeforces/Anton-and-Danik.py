count_A=0
count_D=0

n=int(input())
str=input()

for i in range(len(str)):
    if str[i] == 'A':
        count_A+=1
    elif str[i] == 'D':
        count_D+=1
if count_A>count_D:
    print("Anton")
elif count_D>count_A:
    print("Danik")
else:
    print("Friendship")