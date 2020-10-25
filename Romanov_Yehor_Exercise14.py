# Entering input and making from string all UPPER case:
input_string = input('[!] INPUT: Please enter your value (only string type): ')
upper_string = input_string.upper()


# Function that count letters in string:
def letter_counter(x):
    return upper_string.count(x)


# For cycle that check every letter for duplicates by the previous function:
for i in upper_string:
    if (letter_counter(i) > 1):
        output_value = True
        break
    else:
        output_value = False

# Printing output (the result of program):
print('[/] OUTPUT: Your result is: ', output_value)
