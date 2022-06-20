# Завдання: у наведеному коді додати обробку виключення
#           ZeroDivisionError при спробі поділити на 0
#           Замінити результат текстом про спробу поділити на 0 та надати
#           можливість продовжувати виконання програми
#
# Приклад виконання:
#
#     5 / 3 = 1.6666666666666667
#     653 / 4 = 163.25
#     216 / 2 = 108.0
#     207 / 0 = can't divide by 0
#     119 / 4 = 29.75
#     641 / 4 = 160.25
#     669 / 1 = 669.0
#     400 / 3 = 133.33333333333334
#     271 / 0 = can't divide by 0
#     415 / 4 = 103.75

import random
import time


def main():

    divisors = range(5)
    for _ in range(20):
        num = random.randint(0, 1000)
        divisor = random.choice(divisors)
        try:
            result = num / divisor
            print(f"{num} / {divisor} = {result}")
            time.sleep(1)

        except ZeroDivisionError:
            print("can't divide by 0")

if __name__ == "__main__":
    main()