n,l=map(int, input().split())
lst=list(map(int, input().split()))
lst.sort()
max_digit=0
for i in range(0, len(lst)-1):
    if lst[i+1]-lst[i]>max_digit:
        max_digit=lst[i+1]-lst[i]
max_digit/=2
result = "{:.10f}".format(max(max_digit, lst[0], l-lst[n-1]))
print(result)