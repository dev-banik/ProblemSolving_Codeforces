m_count,c_count=0,0
t=int(input())
for i in range(0, t):
    m,c=map(int, input().split())
    if m>c:
        m_count+=1
    elif m<c:
        c_count+=1
if m_count>c_count:
    print("Mishka")
elif m_count<c_count:
    print("Chris")
else:
    print("Friendship is magic!^^")