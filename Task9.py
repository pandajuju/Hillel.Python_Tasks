# Завдання: надати можливість викликати fibonnaci функцію
#           через HTTP endpoint /fib/<NUM>, у відповідь буде
#           надсилатись послідовнісь елементів ряду Фібоначчі
#
# наприклад: request: http://localhost:5000/fib/7
#            response: "[0, 1, 1, 2, 3, 5, 8]"
#
# замінити тіло у функції з pass інструкцією

from flask import Flask

app = Flask(__name__)

def fibonacci(N):
    if (N <= 1):
        return N
    else:
        return (fibonacci(N - 1) + fibonacci(N - 2))

@app.route("/fib/<int:Num>")
def fib_handler(Num):
    a = []
    for i in range(Num):
        a.append(fibonacci(i))

    return str(a)

app.run(debug=True)