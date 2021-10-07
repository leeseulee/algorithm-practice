import math

def is_prime_number(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True


def solution(numbers):
    answer = 0
    return answer