ans=0
n=int(input())
for i in range(0, n):
    s=input()
    if s=='Tetrahedron':
        ans+=4
    elif s=='Cube':
        ans+=6
    elif s=='Octahedron':
        ans+=8
    elif s=='Dodecahedron':
        ans+=12
    elif s=='Icosahedron':
        ans+=20
print(ans)