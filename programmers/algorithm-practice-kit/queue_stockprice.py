def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        cnt = 0
        for price in prices[i + 1:]:
            cnt += 1
            if price < prices[i]: break
        answer[i] = cnt
    return answer
