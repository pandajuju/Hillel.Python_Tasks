for i in range(10):
    text = input('Введіть текст:')
    if text == '':
        print('Введіть текст!')
        continue
    text_split = text.split()
    text_sorted = []
    for i in range(len(text_split)):
        text_sorted.append(''.join(sorted(text_split[i])))

    text_sorted = ' '.join(sorted(text_sorted))

    print(text_sorted)
