# Importing from heapq library two functions: min (nsmallest) and max (nlargest):
from heapq import nsmallest, nlargest


# Entering input and making from input set:
input_set = input('[!] INPUT: Please enter your values (Float and Integer types) in set here: ')
eval_set = eval(input_set)


# Function that find minimum and maximum of set and printing that:
def min_max(set1, set2):
    minimum = nsmallest(1, set1)
    maximum = nlargest(1, set2)
    print('[/] OUTPUT:'
          '\n', 'Your minimum value is:', minimum,
          '\n', 'Your maximum value is:', maximum
          )

# Printing output by the activation of function:
min_max(eval_set, eval_set)
