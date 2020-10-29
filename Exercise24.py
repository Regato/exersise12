# Entering string data into the system and reversing this string data:
input_string = input('[!] INPUT: Please enter any string text: ')
output_string = input_string[-1:: -1]


# Creating or re-writing new file by the open function (with write mode):
# Writing into file reversed string:
# Closing file:
output_file = open('output.txt', 'w')
output_file.write(output_string)
output_file.close()


# Opening file with read mode:
# Printing opened file:
# Closing file:
output_file = open('output.txt', 'r')
print('[/] OUTPUT: Your output is ready in the file:', output_file.read())
output_file.close()
