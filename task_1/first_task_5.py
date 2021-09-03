# Как вывести на экран последние 30 строк файла?
from collections import deque

with open("big_file.csv") as file:
    for line in deque(file, 30):
        print(line.strip())

# для командной строки linux: tail -n30 big_file.csv
