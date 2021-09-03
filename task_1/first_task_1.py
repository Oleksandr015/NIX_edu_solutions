# Как удалить дубли строк из файла?
list_duplicates = []
example_doc = open('with_duplicates.csv', 'r')
final_doc = open('no_duplicates.csv', 'w')

for line in example_doc:
    if line in list_duplicates:
        continue
    else:
        final_doc.write(line)
        list_duplicates.append(line)

example_doc.close()
final_doc.close()


# для командной строки linux: sort -u with_duplicates.csv или sort with_duplicates.csv | uniq
