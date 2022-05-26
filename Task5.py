while True:
  import random
  n = int(input('Введіть довжину листа:'))
  if n < 10 or n > 50:
      print('Невірний ввод. Спробуйте ще раз!')
      continue

  list_1 = []
  for i in range(n):
    list_1.append(50 + (round(random.random() * 100) % 50))
    for i in range(n - 1):
        for j in range(i+1, len(list_1)):
            if list_1[i] < list_1[j]:
                tmp = list_1[i]
                list_1[i] = list_1[j]
                list_1[j] = tmp
  print(list_1)


