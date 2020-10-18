# Importing json library
import json

# Variables with: input data, json loads data and empty dictionary
input_dict = input()
json_dict = dict(json.loads(input_dict))
output_dict = {}

# Reversing keys and values in dictionary
for key, value in list(json_dict.items()):
    output_dict.update({value: key})

# Printing output (reversed) dictionary:
print(output_dict)
