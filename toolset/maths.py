def factorial(n):
    if n < 0:
      raise Exception(f"Невірний ввод")

    factorial = 1

    for i in range(2, n+1):
        factorial = factorial*i

    return factorial


def convert_to_celsius(value):
    """Converts degrees value from fahrenheit celsius to."""
    return (value - 32) / 1.8


def convert_to_fahrengeit(value):
    """Converts degrees value from celsius to fahrenheit."""
    return value * 1.8 + 32


def fibonacci(N):
    if (N <= 1):
        return N
    else:
        return (fibonacci(N - 1) + fibonacci(N - 2))


def fibonacci_seq(n):
    a = []

    for i in range(n):
        a.append(fibonacci(i))

    return str(a)