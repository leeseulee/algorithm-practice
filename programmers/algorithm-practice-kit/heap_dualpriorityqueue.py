import heapq


def solution(operations):
    h = []
    for operation in operations:
        optr, opnd = operation.split()
        if optr == 'I':
            heapq.heappush(h, int(opnd))
        elif optr == 'D' and len(h) > 0:
            if opnd == '-1':
                heapq.heappop(h)
            else:
                h.sort()
                h.pop()

    answer = [0, 0]
    if len(h) > 0:
        h.sort()
        answer = [h[-1], h[0]]

    return answer