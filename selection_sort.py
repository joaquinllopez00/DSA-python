#BIG O of Selection Sort is => O(n^2)


def findSmallest(arr):
  smallest = arr[0] #stores smallest val
  smallest_index = 0 # stores smallest index
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index


def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = findSmallest(arr) # finds smallest
    newArr.append(arr.pop(smallest)) #adds to new arr
  print(newArr)
  return newArr

selectionSort([3,77,6,8,33,5]) # => [3,5,6,8,33,77]
selectionSort(['hello', 'what', 'are', 'you', 'doing']) # => ['are', 'doing', 'hello', 'what', 'you']
