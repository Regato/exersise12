# Entering data and splitting this data (Input and Split variables):
input_list = input('[!] Input: Please enter any integer numbers and separate them by the comma ",": ')
split_list = input_list.split(',')


# Dict comprehension with boolean-check: "Is entered number happy (number that includes 7)?"
output_list = {int(x): True if ('7' in x) else False for x in split_list}
print('[/] Output: Your dict is: ', output_list)
