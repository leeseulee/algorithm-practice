import math

def is_prime_number(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True

def get_prime_numbers(n):
  arr = [True] * (n + 1)
  arr[1] = False

  for i in range(2, int(math.sqrt(n))+1):
    if not arr[i]: continue
    for j in range(i+1, n+1):
      if arr[j] and j % i == 0:
        arr[j] = False

  result = []
  for i in range(len(arr)):
    if arr[i]: result.append(i)

  return result