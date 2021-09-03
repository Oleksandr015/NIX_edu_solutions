# Как дописать содержимое одного текстового файла в конец второго?

with open('first_doc.csv', 'r') as file1, open('second_doc.csv', 'a') as file2:
    for line in file1:
        file2.write('\n' + line)



# для командной строки linux: second_doc.csv >> first_doc.csv