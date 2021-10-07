n, m = map(int, input().split())
a, b, d = map(int, input().split())
coords = []

for _ in range(n):
  coords.append(list(map(int, input().split())))

curr = [a, b]
ds = [(-1, 0), (0, 1), (-1, 0), (0, -1)]
coords[curr[0]][curr[1]] = 2
count = 1

while True:
  prev = curr
  for _ in range(4):
    d = d - 1 if d - 1 >= 0 else 3
    nx = curr[0] + ds[d][0]
    ny = curr[1] + ds[d][1]
    if coords[nx][ny] == 0:
      count += 1
      coords[nx][ny] = 2
      curr = [nx, ny]
      break
  if prev != curr: continue
  nx = curr[0] + (ds[d][0] * -1)
  ny = curr[1] + (ds[d][1] * -1)
  if coords[nx][ny] == 1:
    break
  else:
    curr = [nx, ny]

print(count)
  