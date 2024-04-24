a = input().split()
lst = list(a)
st = set()
for i in range(0, len(lst)):
    if lst[i] not in st:
        st.add(lst[i])
count = len(lst) - len(st)
print(count)