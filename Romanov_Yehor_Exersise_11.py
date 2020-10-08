# Importing simplejson and collections libraries
import simplejson
import collections
# **Variable with input data (string type)**
str_input_list = input()
# Variable that making list from string (from input data) with simplejson
json_loads_list = simplejson.loads(str_input_list)
# Variables that will help to sort output data (with for cycle)
max_value = max(json_loads_list)
min_value = min(json_loads_list)
# Variable that count list elements with collections library
output_count_result = collections.Counter(json_loads_list)

# *For* cycle that printing output result and fully sorting output data:
for i in range(min_value, max_value+1):
    print(i, ':', output_count_result[i] * '*', sep=' ')
