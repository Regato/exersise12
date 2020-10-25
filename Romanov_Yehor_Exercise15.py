# Entering input and making from input set:
input_set = input('[!] INPUT: Please enter your values (with any types) in set here: ')
eval_set = eval(input_set)


# Function that contains set comprehension (with printing every element):
def output_elements(set):
    print('[/] OUTPUT: Elements of set here:')
    comp_set = [print(i) for i in set]

# Printing output by the activation of function:
output_elements(eval_set)
