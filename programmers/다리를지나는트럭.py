def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = []
    i = 0

    # 대기 트럭이 없을 때까지 enqueue
    # - 만약 큐의 길이가 다리 길이랑 같으면 dequeue
    # - 만약 (큐의길이+1)이 다리 길이보다 같거나 작고, (큐의원소합+다음대기트럭무게)가 다리하중무게보다 같거나 작으면, 다음대기트럭을 enqueue
    # - 그렇지 않으면, 0을 enqueue
    while i < len(truck_weights):
        if len(queue) == bridge_length:
            queue.pop(0)
        if len(queue) + 1 <= bridge_length and sum(queue) + truck_weights[i] <= weight:
            queue.append(truck_weights[i])
            i += 1
        else:
            queue.append(0)
        answer += 1
        
    # 대기트럭이 없는데 큐의 길이가 다리 길이보다 짧다면 
    # 다리 길이와 동일해질 때까지 0을 enqueue 반복
    while len(queue) < bridge_length:
        queue.append(0)

    # 큐가 빌 때까지 dequeue 반복
    while len(queue) > 0:
        queue.pop(0)
        answer += 1

    return answer
