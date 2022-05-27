for i in range(10):
    text = input('Введіть текст:')
    if text == '':
        print('Введіть текст!')
        continue
    a = text.split()
    b = []
    for i in range(len(a)):
        b.append(''.join(sorted(a[i])))

    b = ' '.join(sorted(b))

    print(b)
