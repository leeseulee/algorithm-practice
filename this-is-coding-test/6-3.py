n = int(input())
array = []

for _ in range(n):
    a, b = input().split()
    array.append((a, int(b)))

array.sort(key=lambda x: x[1])

for std in array:
    print(std[0], end=' ')
