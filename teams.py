i = int(input())
n = 0
a = 0
    
while n < i:
    k = tuple(map(int, input().split(' ')))   
    if k[0] + k[1] + k[2] >= 2:
        a += 1
    
    n += 1
print(a)

