import math
input = tuple(map(int, input().split(' ')))
n, m, a = input[0], input[1], input[2]

i = math.ceil(n / a)
j = math.ceil(m / a)
   
print(i*j)
    
