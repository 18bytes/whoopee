def permutations(first, second):
  result = []
  for i in range(len(first)):
    for j in range(len(second)):
      result.append(first[i] + ' ' + second[j])
  return result 

FIRST = ["A", "B", "C"]
SECOND = ["D", "E"]
print permutations(FIRST, SECOND)
