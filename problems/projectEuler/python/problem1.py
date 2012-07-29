"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def get_multiples(list):
  result = []
  for item in list:
    if item % 3 is 0 or item % 5 is 0:
      result.append(item)
  return result

DATA = [x for x in range(1, 1000)]
print  sum(get_multiples(DATA))


