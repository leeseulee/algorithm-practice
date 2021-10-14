from collections import deque


def solution(begin, target, words):
    answer = 0
    # target이 words 안에 없을 경우 0 반환
    if target not in words:
        return answer
    # queue = [(word, depth)]
    queue = deque([(begin, 0)])
    visited = set()
    while queue:
        curr = queue.popleft()
        # word가 target 과 같을 경우 depth 리턴
        if curr[0] == target:
            return curr[1]
        for word in words:
            # 이미 방문한 word인지 확인
            if word in visited: continue
            # 한 문자만 다른 단어인지 확인
            compared = map(lambda x: x[0] != x[1], zip(curr[0], word))
            if sum(compared) == 1:
                queue.append((word, curr[1] + 1))
                visited.add(word)
    return answer