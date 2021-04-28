from math import pi
figure = input()
x = float(input())
y = float(input())
area = 0

if figure == "square":
    area = x * x
elif figure == "rectangle":
    area = x * y
elif figure == "circle":
    area = 2 * pi * x
elif figure == "triangle":
    area = x * y / 2

print(f'{area:.3f}')
