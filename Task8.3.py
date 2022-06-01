"""Задача: написати функцію сalculator для двух операндів .

   Деталі:
            * функція приймає три аргумента - лівий операнд, оператор, правий операнд
            * функція повинна повернути результат операції над операндами
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * calculate(2, "+", 2) -> повертає 4
            * calculate("hello world!", "*", 2) -> повертає "hello world!hello world!"
            * calculate(10, ")", 10) -> повертає None
"""

def calculator(left_operand, operator, right_operand):
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    elif operator == '/':
        return left_operand / right_operand
    else:
        return None

print(calculator(left_operand = "hello world!" , operator = "*", right_operand = int("2")))
print(calculator(left_operand = int(2) , operator = "+", right_operand = int("2")))
print(calculator(left_operand = int(10) , operator = ")", right_operand = int("2")))