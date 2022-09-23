n = int(input())
a = 0

for i in range(n):
    j = str(input())
    k = j.replace("X", "")
    if k == '++':
        a += 1
    elif k == '--':
        a -= 1

print(a)
    