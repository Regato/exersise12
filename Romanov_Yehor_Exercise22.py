# Entering data and splitting this data (Input and Split variables):
input_list = input('[!] Input: Please enter any integer numbers and separate them by the comma ",": ')
split_list = input_list.split(',')


# List comprehension with boolean-check: "Is number in list > index of this number?"
output_list = [int(i) for i in split_list if (split_list.index(i) < int(i))]
print('[/] Output: Your list is: ', output_list)
