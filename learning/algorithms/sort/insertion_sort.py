import utils

@utils.measure_time
def insertion_sort(input):
  # Precondition check.
  if input == None: print "Input cannot be None."
  for i in range(2, len(input)):
    num = input[i]
    j = i
    while j > 0 and num < input[j - 1]:
      input[j] = input[j - 1]
      j = (j - 1)
    input[j] = num

if __name__ == '__main__':
  utils.sort(insertion_sort)