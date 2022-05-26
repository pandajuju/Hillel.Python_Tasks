while True:
    import random

    n = int(input('Введіть довжину листа: '))

    if n < 10 or n > 50:
        print('Невірний ввод. Спробуйте ще раз!')
        continue

    list_1 = []
    for _ in range(n):
        list_1.append(50 + (round(random.random() * 100) % 50))
    print(list_1)

    k = 0
    for i in range(1, len(list_1)-1):
        if list_1[i-1] < list_1[i] and list_1[i] > list_1[i+1]:
            k +=1
    print(k)

    exit = input("\nЯкщо хочете продовжити - натисніть ENTER \nВийти - N\n")
    if exit == 'N':
        break