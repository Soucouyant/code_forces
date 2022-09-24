from typing import List

def solver(s: str):
    if '+' in s:
        i = s.split('+')
        i.sort()
        n = ''
        for x in range(len(i)):
            n += i[x]
            n += '+'
        
        print(n[:-1])
    # Edge Case
    else:
        print(s)
        
solver(str(input()))