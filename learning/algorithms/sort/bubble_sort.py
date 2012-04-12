import random_list_generator
# TODO Use same input and compare executaion time

def bubble_sort(input):
  swapped = True

  # Precontion check
  if input == None: print "You must provide a list."
  if len(input) <= 1: return input
  
  while swapped:
    swapped = False # Reset the flag
    for i in range(0, len(input) - 1):
      if input[i] > input[i + 1]:
        # Swap
        temp = input[i]
        input[i] = input[i + 1]
        input[i + 1] = temp
        swapped = True
  return input



if __name__ == '__main__':
  data = random_list_generator.get_random_number_list(5000)
  print "--------------------------"
  print "input:"
  print data
  print "--------------------------"
  print "Sorted result:"
  print bubble_sort(data)
  print "--------------------------"