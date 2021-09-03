'''напишите lambda функцию, которая будет складывать 2 числа:
my_lambda = <ваша лябмда функция>'''

x = lambda a, b: a + b
print(x(3, 5))


# or

def lambda_func(b):
    return lambda a: a + b


mydoubler = lambda_func(3)

print(mydoubler(5))
