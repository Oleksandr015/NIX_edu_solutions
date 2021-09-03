# Как разбить текстовый файл на несколько по 100 строк в каждом?
big_f = open('big_file.csv', 'r')
file_counter = 1
temp_file = open('small_file' + str(file_counter) + ".csv", 'w')
for str_num, string in enumerate(big_f.readlines()):
    if str_num > 0 and str_num % 100 == 0:
        file_counter += 1
        temp_file.close()
        temp_file = open('small_file' + str(file_counter) + ".csv", 'w')
    temp_file.write(string)
temp_file.close()

# from itertools import islice
#
#
# with open('big_file.csv') as text:
#     for str_num, sli in enumerate(iter(lambda: list(islice(text, 100)), []), 1):
#         with open('small_file' + str(str_num), "w") as f:
#             f.writelines(sli)

# для командной строки linux: split -l 100 big_file.csv 100-
