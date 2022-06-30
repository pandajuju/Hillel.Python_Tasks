# Переписати цикл з використанням iter/next функцій
# підказка: idx, s[idx]
s = "Hello world!"
idx = iter(s)
while ch := next(idx):
    if ch == ' ':
        break
    print(ch, end="")
