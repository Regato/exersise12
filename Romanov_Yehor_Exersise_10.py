# **Variables with input and stable data (integer and list types)**
n = int(input())
letters_list = ['p', 'q']
# Variable that will be containing the result of code:
result_list = list()
# Variable to count cycle and give numbers to mix with letters for the result list:
counter = 0

# *While* cycle to count and mix two lists in one:
while (counter != n):
    counter += 1
    result_list.append(letters_list[0] + str(counter))
    result_list.append(letters_list[1] + str(counter))
print(result_list)
