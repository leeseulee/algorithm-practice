COL = 'abcdefgh'

col, row = [w for w in input()]
curr = [int(row), COL.index(col) + 1]

directions = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
count = 0

for d in directions:
  new_row = curr[0] + d[0]
  new_col = curr[1] + d[1]
  
  if new_row < 1 or new_row > 8 or new_col < 1 or new_col > 8: continue
  count += 1

print(count)