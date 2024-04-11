matrix = []

for i in range(5):          
    a = input().split()  
    a = [int(x) for x in a] 
    matrix.append(a)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            x=abs((i+1)-3)
            y=abs((j+1)-3)

print(x+y)