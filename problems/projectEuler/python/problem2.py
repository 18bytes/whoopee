

"""
  Method returns fibonacci series less than 4000000
"""
def fibonacci():
  result = []
  i = 0
  while True:
    if i == 0 or i == 1:
      result.append(i)
    else:
      val = result[i - 1] + result[i - 2]
      if val > 4000000:
        return result
      result.append(val)
    i = i + 1
  return result

"""
  Method return sum of even numbers
"""
def sum_of_even(numbers):
  sum = 0
  for i in numbers:
    if (i % 2) == 0:
      sum = sum + i
  return sum
  
print sum_of_even(fibonacci())
  

