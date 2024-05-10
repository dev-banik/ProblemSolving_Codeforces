g_name=str(input())
h_name=str(input())
pile=str(input())
s=g_name+h_name
s=''.join(sorted(s))
pile=''.join(sorted(pile))
if s==pile:
    print("YES")
else:
    print("NO")