num = input('Введіть послідовність чисел: ')
arr_str = num.split(' ')

arr_num = list(map(int, arr_str))
arr_filter = filter(lambda x: x>10, arr_num)
result = ' '.join(map(str, arr_filter))


print(result)