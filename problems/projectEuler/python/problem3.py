# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def get_primefactor(input):
  result = []
  value = input
  for num in range(2, input):
    if is_prime(num) and value % num is 0 and len(result) > 0 and result[len(result) - 1] > num:
      result.append(num)
      print "Value: " + str(value)
      result += get_primefactor(value / num)

  return result


def is_prime(num):
  for i in range(2, num):
    if num % i is 0: return False

  return True


print get_primefactor(12)
