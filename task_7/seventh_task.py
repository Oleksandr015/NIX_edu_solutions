'''Напишите функцию, которая делает return строки приветствия людей из разных стран на разных языках, в зависимости от страны человека.
Вызовите функцию используя map
Требование: используйте map
Для примера можете взять этот список юзеров:
users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
]
На выходе с использованием users_list, после использования map вы должны получить результат iterable с такими приветствиями:
Привет, Александр!
Hello, James!
Hola, Daniella!
Hello, Someone, but I do not know where are you from!'''

users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
]


def say_hello(x):
    if x[1] == 'ru':
        print('Привет, %s!' % x[0])
    elif x[1] == 'us':
        print('Hello, %s!' % x[0])
    elif x[1] == 'es':
        print('Hola, %s!' % x[0])
    else:
        print('Hello, %s, but I do not know where are you from!' % x[0])




if __name__ == '__main__':
    result = map(say_hello, users_list)
    print(list(result))