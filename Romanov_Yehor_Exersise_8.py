# Importing simplejson and collections libraries
import simplejson
# **Variables with input data (string type)**
str_input_list = input()
# Variable that making list from string (from input data) with simplejson
json_loads_list = simplejson.loads(str_input_list)
# Variables that will help to sort output data (max and min values)
min_value = min(json_loads_list)
max_value = max(json_loads_list)
# Variables that containing empty lists (temporary and result - output)
temporary_list = list()
output_list = list()

# *For* cycle to count and sort duplicates in list:
for i in range(min_value, max_value+1):
    element_counter = json_loads_list.count(i)
    for j in range(element_counter):
        temporary_list.append(i)
    output_list.append(temporary_list)
    temporary_list = list()
print(output_list)
