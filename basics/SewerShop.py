tables_count = float(input())
tables_lenght = float(input())
tables_width = float(input())

rectangle_cloth = tables_count * (tables_lenght + 2 * 0.3) * (tables_width + 2 * 0.3)
square_cloth = tables_count * (tables_lenght/ 2) * (tables_lenght / 2)

price_in_usd = (rectangle_cloth * 7) + (square_cloth * 9)
price_in_bgn = price_in_usd * 1.85

print(f'{price_in_usd:.2f} USD')
print(f'{price_in_bgn:.2f} BGN')
