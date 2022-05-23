for i in range(10):
  text = input('Введіть текст:')
  letter = input('Введіть літеру:')
  if len(letter) > 1:
    print(f'Введено більше однієї літери.Спробуйте ще раз!')
    continue

  count = 0
  for i in text :
    if i == letter:
      count = count + 1

  if count == 0:
      print(f'строка не містить літеру {letter}')
  elif count < 10:
    print(f'строка містить літеру {letter} до 10 разів ({count} разів)')
  elif count < 20:
      print(f'строка містить літеру {letter} до 20 раз ({count} разів)')
  else:
      print(f'строка містить літеру {letter} більше 20 разів ({count} разів)')