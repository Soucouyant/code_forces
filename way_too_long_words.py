i = int(input())
k = 0

while k < i:
    j = str(input())
    
    if len(j) > 10:
        l = j[:1]
        m = len(j) - 2
        n = j[-1:]
        
        print(l,m,n, sep='')
        
    else:
        print(j)
    k += 1
    