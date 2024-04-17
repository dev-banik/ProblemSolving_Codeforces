total_passenger=0
count_passenger=0
n=int(input())
for i in range(0, n):
    ab=input().split()
    total_passenger-=int(ab[0])
    total_passenger+=int(ab[1])
    if total_passenger>=count_passenger:
        count_passenger=total_passenger

print(count_passenger)