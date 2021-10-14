import math
from itertools import permutations

# 소수 판별
# 1과 자기자신 만 약수로 가지기 때문에 다른 수로 나눴을 때는 나머지가 0이 아니라는 성질 이용
# 해당숫자의 절반까지만 확인해도 ok
# (자기자신을 제외하고 절반을 초과하는 숫자에서 나눴을때 나머지가 0이되는 숫자는 나올수가 없으므로)


def is_prime_number(n):
    # 0과 1은 소수가 아님
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    # 가능한 숫자 조합
    availables = set()
    # 소수
    prime_numbers = set()
    # 1부터 numbers의 길이까지 순환
    for i in range(1, len(numbers) + 1):
        # 각 자리수마다 가능한 순열 순환
        for p in permutations(numbers, i):
            num = int(''.join(p))
            # 이미 확인한 숫자조합은 건너뜀
            if num in availables:
                continue
            availables.add(num)
            if is_prime_number(num):
                prime_numbers.add(num)
    return len(prime_numbers)