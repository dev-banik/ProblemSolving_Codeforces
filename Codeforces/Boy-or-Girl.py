str=input()
str_rmv = ""
for char in str:
    if char not in str_rmv:
        str_rmv=str_rmv+char

if len(str_rmv)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")