# Importing from collections library Counter function:
from collections import Counter


# Opening file with write mode and writing quote in this file:
# Closing opened file:
output_file = open('input.txt', 'w')
output_file.write('One of the penalties for refusing to '
                  'participate in politics is that you '
                  'end up being governed by your inferiors'
                  )
output_file.close()


# Opening file with read mode and reading quote in this file:
output_file = open('input.txt', 'r')
read_file = output_file.read()

# Splitting this text by split function:
# Counting ALL words in text by len function:
# Counting every word in text separately:
split_file = read_file.split()
len_file = len(split_file)
counter_file = Counter(split_file)

# Closing opened file:
output_file.close()


# Printing output of program:
print('[/] OUTPUT: ',
      '\n', 'Count of all words is:', len_file,
      '\n', 'Separate count of every word:'
      )

# It is part of printing:
for i in counter_file:
    print(f'  {i}: ', counter_file[i])
