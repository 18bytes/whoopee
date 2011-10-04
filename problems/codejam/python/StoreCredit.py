

def store_credit1(credit, data):
  result = []
  for i in range(1,len(data)):
    print i
    for j in range(i+1, len(data)):
      print "j: " + str(j)
      if data[i] + data[j] == credit:
        print data[i] + data[j]
        return [i, j]
def store_credit2(C, L):
  for i in xrange(len(L) - 1):
    try:
      i2 = L.index(C - L[i], i + 1)
      return [i+1, i2+1]
    except ValueError:
      pass
  return None



if __name__ == "__main__":
  credit = 100
  data = [5, 2, 21, 34, 79, 43]
  print store_credit1(credit, data)
  print store_credit2(credit, data)
    
    
