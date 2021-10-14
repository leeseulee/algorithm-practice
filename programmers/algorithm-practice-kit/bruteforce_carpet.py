def solution(brown, yellow):
    number = (brown - 4) / 2
    for i in range(1, int(number / 2) + 1):
        if (i * (number - i)) == yellow:
            answer = [i + 2, number - i + 2]
            break
    return sorted(answer, reverse=True)