# Дан список из словарей в формате [{'name': 'Oleg', 'age': 23}, {'name': 'Vasya', 'age': 19}]
# Отсортируйте список по возрасту людей, чтобы получилось [{'name': 'Vasya', 'age': 19}, {'name': 'Oleg', 'age': 23}]
# Используйте sorted и lambda

def list_sort(list_of_dict):
    return sorted(list_of_dict, key=lambda k: k['age'])


if __name__ == '__main__':
    print(list_sort([{'name': 'Oleg', 'age': 23}, {'name': 'Vasya', 'age': 19}]))
