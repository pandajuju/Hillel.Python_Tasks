
for i in range(10):
  text = input('Введіть текст:')
  letter = input('Введіть літеру:')
  if len(letter) > 1:
    print(f'Введено більше однієї літери.Спробуйте ще раз!')
    letter = input('Введіть літеру:')
    continue
  count = 0
  answer = 0
  for i in text :
    if i == letter:
      count = count + 1
  if count == 0:
      print(f'строка не містить літеру {letter}')
  else:
    if count < 10:
      answer = 'до 10'
    elif count < 20:
      answer = 'до 20'
    else:
      answer = 'більше 20'
    print(f'строка містить літеру {letter} {answer} разів ({count} разів)')