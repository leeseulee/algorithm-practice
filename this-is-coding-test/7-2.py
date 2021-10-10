import sys

n = int(input())
narr = list(map(int, sys.stdin.readline().rstrip().split()))
narr.sort()

m = int(input())
marr = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


for v in marr:
    r = binary_search(narr, v)
    if r == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
