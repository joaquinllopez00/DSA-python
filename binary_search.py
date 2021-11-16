
#RANDOM TEST TO MAKE SURE MY SSH KEY IS WORKING 

#Definition
# Binary search is an algorithm; its input is a sorted list of elements
# (I’ll explain later why it needs to be sorted). If an element you’re
# looking for is in that list, binary search returns the position
# where it’s located. Otherwise, binary search returns null


# With binary search, you guess the middle number and eliminate half the
# remaining numbers every time.


###
# WORST CASE

# log n 
###

#Binary Searches only work when your list is in sorted order


#######EXAMPLE

def binary_search(list, item):
  low = 0                 #set initial low and high
  high = len(list) - 1
  while low <= high: #goes until you've narrowed it down to one el
    mid = (low + high) // 2 #checks mid el
    guess = list[mid] #
    if guess == item: #found item 
      return mid
    if guess > item:  #update high if guess was too high
      high = mid - 1
    else: #update low if guess was too low
      low = mid + 1
  return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, 33)) # => None   
