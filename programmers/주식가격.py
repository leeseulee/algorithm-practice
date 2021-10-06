def solution(genres, plays):
    result = {}
    # result = {장르명: [속한 노래가 재생된 총 횟수, (노래 고유번호, 노래 재생횟수) 튜플로 이루어진 배열]}
    # result = {'classic': [1450, [(0, 500), (2, 150), (3, 800)]], 'pop': [3100, [(1, 600), (4, 2500)]]}
    for i, val in enumerate(genres):
        if val in result:
            result[val][0] += plays[i]
            result[val][1].append((i, plays[i]))
        else:
            result[val] = [plays[i], [(i, plays[i])]]

    answer = []
    # 장르의 총 재생횟수 기준으로 배열한 해시의 value를 순환하면서 -> [[1450, [(0, 500), (2, 150), (3, 800)]], [3100, [(1, 600), (4, 2500)]]]
    # 각 value의 2번째 원소((노래 고유번호, 노래 재생횟수) 튜플로 이루어진 배열)를 노래 재생횟수 기준으로 배열해서 -> [(3, 800), (0, 500), (2, 150)]
    # 앞에서 2번째까지의 고유번호만 추출 -> [3, 0]
    # 추출한 배열을 answer에 merge
    for r in sorted(result.values(), key=lambda x: x[0], reverse=True):
        answer += list(map(lambda x: x[0], sorted(r[1], key=lambda x: x[1], reverse=True)[:2]))

    return answer
