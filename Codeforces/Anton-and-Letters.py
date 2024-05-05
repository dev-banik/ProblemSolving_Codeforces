s=input()
string = s.replace('{','').replace('}','').replace(',','')
p = ""
for char in string:
    if char not in p:
        p = p+char
p=p.replace(' ','')
print(len(p))