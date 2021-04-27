yards_area = int(input())

price_no_discount = float(yards_area * 7.61)
discount = float(price_no_discount * 0.18)
price_discount = float(price_no_discount - discount)

print(f'The final price is: {price_discount:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')
