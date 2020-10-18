import json

input_dict = input()
output_dict = dict(json.loads(input_dict))

for key, value in list(output_dict.items()):
    if (value == 'None'):
        del output_dict[key]

print(output_dict)