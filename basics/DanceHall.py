import math
hall_length = float(input())
hall_width = float(input())
wardrobe_side = float(input())

hall_area = hall_length * 100 * hall_width * 100
wardrobe_area = wardrobe_side * 100 * wardrobe_side * 100
bench_area = hall_area / 10

dance_area = hall_area - (wardrobe_area + bench_area)

dancer_needed_area = 40 + 7000
dancers = math.floor(dance_area / dancer_needed_area)

print(dancers)
