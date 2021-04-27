x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

side_one = abs(x1 - x2)
side_two = abs(y1 - y2)

area = side_one * side_two
parameter = 2 * side_one + 2 * side_two

print(f'{area:.2f}')
print(f'{parameter:.2f}')
