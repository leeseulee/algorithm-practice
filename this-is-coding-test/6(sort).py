array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# selection sort
for i in range(len(array)):
    min_i = i
    for j in range(i + 1, len(array)):
        if array[min_i] > array[j]:
            min_i = j
    array[i], array[min_i] = array[min_i], array[i]

# insertion sort
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break


# quick sort
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


quick_sort(array)

# count sort
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

array = []
for j in range(len(count)):
    if count[j] > 0:
        array += [j] * count[j]

print(array)