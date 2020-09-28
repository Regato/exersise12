# **Variables with input (entering) data**
first_year = int(input())
last_year = int(input())
# Variable that contains first and last years subtraction:
year_subtraction = (last_year - first_year)
# Variable that count every year  in years range:
year_counter = (first_year)
# Variable that contains result of code:
result_list = list()

# *For* cycle to detect any leap year in year subtraction range:
for i in range(year_subtraction + 1):
    if (year_counter % 4 == 0):
        result_list.append(year_counter)
    year_counter += 1
print(result_list)
