while True:
    n = int(input('Введіть число для обчислення факторіалу:'))

    if n < 0:
      print(f"Невірний ввод")
      continue

    factorial = 1
    for i in range(2, n+1):
      factorial = factorial*i
    print((f"{n}! == {factorial}"))
