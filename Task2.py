import math

Cx = int(input("Введіть Cx:"))
Cy = int(input("Введіть  Cy:"))

r1 = int(input("Введіть радіус r1:"))
r2 = int(input("Введіть  радіус r2:"))

Px = int(input("Введіть Px:"))
Py = int(input("Введіть Py:"))

L = math.sqrt((Px-Cx) ** 2 + (Py-Cy) ** 2)

a = 0
if r1 < L < r2:
    a = 'належить'
else:
    a = 'не належить'

print("Точка ({0}, {1}) {2} кільцю за центром у точці ({3}, {4}), та r1 = {5}, r2 = {6}".format(Px, Py, a, Cx, Cy, r1, r2))