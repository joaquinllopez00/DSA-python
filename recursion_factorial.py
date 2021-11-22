def fact(x):
  if (x == 1):
    return 1 # base case
  else: # recursion case
    return x * fact(x-1)
    

"""
Visualized example


fact(3) => returns x * fact(3-1)
fact(2) => returns x * fact(2-1)
fact(1) => returns 1
"""

print(fact(3)) #=> 6
print(fact(6)) #=> 720
print(fact(998)) #=> a lot. 998 is recursion depth limit


