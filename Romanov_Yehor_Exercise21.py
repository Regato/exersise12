# 1st Exercise:
input_data = input('1st input: ').split()
output_data = [len(i) for i in input_data]
print('1st output:', output_data)


# 2nd Exercise:
input_data = input('2nd input: ').split(',')
output_data = [abs(float(i)) for i in input_data]
print('2nd output:', output_data)


# 3rd Exercise:
output_data = [(i ** 2) for i in range(1, 11) if (i % 2 == 0)]
print('3rd output:', output_data)


# 4th Exercise:
output_data = [i for i in range(1, 11) if ((i ** 3) % 4 == 0)]
print('4th output:', output_data)


# 5th Exercise:
first_list = [i for i in range(1, 22)]
second_list = [i for i in first_list if (i % 2 != 0)]
third_list = first_list[7: 14: 1]
print('5th output:', '\n', first_list, '\n', second_list, '\n', third_list)


# 6th Exercise:
output_data = [(i ** 2) for i in range(1, 11) if (30 < (i ** 2) < 70)]
print('6th output:', output_data)


# 7th Exercise:
encrypt_string = '!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI'
reverse_string = encrypt_string[-1:: -1]
output_data = reverse_string.replace('X', '')
print('7th output:', output_data)