# Row Inputs
row_0 = tuple(map(int,input().split(' ')))
row_1 = tuple(map(int,input().split(' ')))
row_2 = tuple(map(int,input().split(' ')))
row_3 = tuple(map(int,input().split(' ')))
row_4 = tuple(map(int,input().split(' ')))

rows = (row_0, row_1, row_2, row_3, row_4)

Y_finder = 0
for i in range(5):
    nthRow = rows[i]
    if nthRow[0] + nthRow[1] + nthRow[2] + nthRow[3] + nthRow[4] == 1:
        Y_finder = i

X_finder = 0
for i in range(5):
    nthRow = rows[Y_finder]
    if nthRow[i] == 1:
        X_finder = i

onePos = (X_finder + 1, Y_finder + 1)

toMoveX = onePos[0] - 3
toMoveY = onePos[1] - 3

finalToMove = abs(toMoveX) + abs(toMoveY)
print(finalToMove)
