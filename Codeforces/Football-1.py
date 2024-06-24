team_a_count,team_b_count=0,0
n=int(input())
team = [input() for i in range(n)]
team_a=team[0]
for i in team:
    if i==team_a:
        team_a_count+=1
    else:
        team_b=i
        team_b_count+=1
print(team_a) if team_a_count>team_b_count else print(team_b)