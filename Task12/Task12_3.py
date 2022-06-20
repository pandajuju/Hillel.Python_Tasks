# Завдання: надайте можливість роботи наведеного кода у разі вводу
#           строк. Використайте довжину строки у такому випадку.
#
# Приклад:
#
# a + b = ?
# Input: 3
# Input: 5
# 3 + 5 = 8
# Input: 3
# Input: def
# 3 + 3 = 6
# Input: abc
# Input: def
# 3 + 3 = 6

def get_value_from_user():
    inp = input("Input: ")
    try:
        return int(inp)
    except ValueError:
        return len(inp)

if __name__ == "__main__":

    print("a + b = ?")

for _ in range(2):
    v1 = get_value_from_user()
    v2 = get_value_from_user()
    print(f"{v1} + {v2} = {v1+v2}")

