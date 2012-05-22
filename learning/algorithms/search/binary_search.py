INPUT = [2, 5, 9, 10, 22, 99]

def binary_search(arr, search_for, left, right):
  result = 0
  # Precondtion check.
  mid = (left + right) / 2
  if arr[mid] > search_for:
    return binary_search(arr, search_for, left, mid -1)
  elif arr[mid] < search_for:
    return binary_search(arr, search_for, mid + 1, right)
  else:
    return mid


if __name__ == '__main__':
  print binary_search(INPUT, 5, 0, len(INPUT) - 1)