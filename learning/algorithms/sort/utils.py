import random
import time

def sort(fn):
  data = get_random_number_list(500)
  print "--------------------------"
  print "input:"
  print data
  print "--------------------------"
  print "Sorted result:"
  fn(data)
  print data
  print "--------------------------"

def get_random_number_list(size):
  result = []
  for i in range(0, size):
    result.append(random.randint(1, 1000))
  return result

# Decorator to measure time and print the result.
def measure_time(fn):
  def measure(*args):
    start = time.time()
    fn(*args)
    end = time.time()
    print "Time taken to run %s method is %r seconds." % ( fn.__name__ , round((end - start), 2))
  return measure