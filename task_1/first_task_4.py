# Как вывести на экран первые 30 строк файла?

from itertools import islice

with open("big_file.csv") as file:
    head = "".join(list(islice(file, 30)))
print(head)

# для командной строки linux: head -n30 big_file.csv
