# Alphabet constant string and counting of letters from this string by len function:
alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
len_string = len(alphabet_string)

# List comprehension from alphabet_string letters:
alphabet_comp = [item for item in alphabet_string]


# For cycle with creating and writing of new files:
for i in range(1, len_string+1):
    output_file = open((str(i) + '.txt'), 'w')
    output_file.write(alphabet_comp[i-1])
    output_file.close()


# For cycle with reading of ready to use files:
for i in range(1, len_string + 1):
    output_file = open((str(i) + '.txt'), 'r')
    print(f'[/] OUTPUT: Your output is ready in the "{i}" file:', output_file.read())
    output_file.close()
