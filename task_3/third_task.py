# Написать свой декоратор, который будет отлавливать ошибки, полученные в ходе выполнения обёрнутой функции,
# логгировать их и делать raise отловленной ошибки

import random
import logging


def my_decorator(fn):
    def wrapped():
        logging.basicConfig(filename="Errors.log", format='%(asctime)s - %(message)s \n', level=logging.ERROR)
        log = logging.getLogger("exception")
        try:
            return fn()
        except Exception as e:
            print("Error:", e)
            log.exception(f"Divisor is not divisible by 3. Try again!")

    return wrapped


@my_decorator
def my_func():
    while True:
        divisor = random.randint(0, 9)
        if divisor % 3 != 0:
            raise Exception(f'Number {divisor} is not divisible by 3. Try again!')

        print(divisor % 3)


if __name__ == '__main__':

   my_func()
