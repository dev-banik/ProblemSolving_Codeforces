t=int(input())
for _ in range(0, t):
    a,b,c=map(int, input().split())
    max_product=0
    for i in range(6):
        for j in range(6-i):
            k=5-i-j
            if k>=0:
                new_a=a+i
                new_b=b+j
                new_c=c+k
                product=new_a*new_b*new_c
                max_product=max(max_product, product)
    print(max_product)