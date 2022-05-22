n = int(input('Введіть число для обчислення факторіалу:'))
factorial = 1
if n < 0:
    print(f"Невірний ввод")
else:
    while n >= 0:
        if n == 0:
          factorial = 1
        else:
          for i in range(2, n+1):
            factorial = factorial*i
        print("{0}! == {1}".format(n, factorial))
        break