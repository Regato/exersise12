# 1st Exercise:
input_data = input('** 1st input, Please enter any string sentence: ')
split_data = input_data.split()

output_data = [len(i) for i in split_data]
print('1st output, Your result list is: ', output_data, '\n')



# 2nd Exercise:
input_data = input('** 2nd input, Enter any float numbers and separate them by the comma ",": ')
split_data = input_data.split(',')

output_data = [abs(float(i)) for i in split_data]
print('2nd output, Your result list is: ', output_data, '\n')



# 3rd Exercise:
output_data = [(i ** 2) for i in range(1, 11) if (i % 2 == 0)]
print('** 3rd output, Your result list is: ', output_data, '\n')



# 4th Exercise:
output_data = [i for i in range(1, 11) if ((i ** 3) % 4 == 0)]
print('** 4th output, Your result list is: ', output_data, '\n')



# 5th Exercise:
first_list = [i for i in range(1, 22)]
second_list = [i for i in first_list if (i % 2 != 0)]
third_list = first_list[7: 14: 1]
print('** 5th output:',
      '\n', 'First list: ', first_list,
      '\n', 'Second list: ', second_list,
      '\n', 'Third list: ', third_list,
      '\n')



# 6th Exercise:
output_data = [(i ** 2) for i in range(1, 11) if (30 < (i ** 2) < 70)]
print('** 6th output, Your result list is: ', output_data, '\n')



# 7th Exercise:
encrypt_string = '!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI'
reverse_string = encrypt_string[-1:: -1]
output_data = reverse_string.replace('X', '')
print('** 7th output, Your result string is: ', output_data)
