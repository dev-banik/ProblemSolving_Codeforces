import math
red, blue=map(int, input().split())
days=min(red, blue)
remaining=math.floor((max(red, blue)-days)/2)
print(days, remaining)