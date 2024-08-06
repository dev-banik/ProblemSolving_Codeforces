t = int(input())
for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    outcomes = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]    
    win_count = 0    
    for a_first, b_first, a_second, b_second in outcomes:
        suneet_wins = 0
        slavic_wins = 0
        if a_first > b_first:
            suneet_wins += 1
        elif b_first > a_first:
            slavic_wins += 1
        if a_second > b_second:
            suneet_wins += 1
        elif b_second > a_second:
            slavic_wins += 1
        if suneet_wins > slavic_wins:
            win_count += 1
    print(win_count)