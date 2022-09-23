# Iterators
i = 0 
s = 0

# Inputs Line 1: n and k
inputs = tuple(map(int, input().split(' ')))
n = inputs[0]
k = inputs[1]

# Scores Line 2: a
a = tuple(map(int, input().split(' ')))

# Code
while i < n:
    if a[i] >= a[k - 1] and a[i] > 0:
        s += 1
    i += 1

print(s)