def factorial(n):
    if n < 0:
      raise Exception(f"Невірний ввод")

    factorial = 1

    for i in range(2, n+1):
        factorial = factorial*i

    return factorial


def to_celsius(d):
    """Converts degrees value from fahrenheit celsius to."""
    return (d - 32) / 1.8


def to_fahrengeit(d):
    """Converts degrees value from celsius to fahrenheit."""
    return d * 1.8 + 32


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