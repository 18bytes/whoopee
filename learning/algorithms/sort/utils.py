import random

def get_random_number_list(size):
  result = []
  for i in range(0, size):
    result.append(random.randint(1, 1000))
  return result
