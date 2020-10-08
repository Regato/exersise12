# Importing simplejson library to use loads function
import simplejson
# **Variables with input data (string type)**
str_input_list = input()
# Making from string to list with simplejson loads function
json_loads_list1 = simplejson.loads(str_input_list)
# This variable will contain the result of program
output_list = list()

# *For* cycle to detect list in list and to make new list without lists:
for i in json_loads_list1:
    if type(i) == list:
        list_counter = str(i).count('[')
        string_value = str(i)
        unpack_value = '[' + string_value[list_counter: -list_counter: 1] + ']'
        json_loads_list2 = simplejson.loads(unpack_value)
        output_list += json_loads_list2
    elif type(i) != list:
        output_list.append(i)
print(list(output_list))
