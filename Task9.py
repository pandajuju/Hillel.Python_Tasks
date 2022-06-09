# Завдання: надати можливість викликати fibonnaci функцію
#           через HTTP endpoint /fib/<NUM>, у відповідь буде
#           надсилатись послідовнісь елементів ряду Фібоначчі
#
# наприклад: request: http://localhost:5000/fib/7
#            response: "[0, 1, 1, 2, 3, 5, 8]"
#
# замінити тіло у функції з pass інструкцією

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/fib/<int:N>")
def fibonacci(N):
    def fibonacci(N):
        if (N <= 1):
            return N
        else:
            return (fibonacci(N - 1) + fibonacci(N - 2))

    a = []
    for i in range(N):
        a.append(fibonacci(i))

    return str(a)
# if __name__ == "main":
app.run(debug=True)