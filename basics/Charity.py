import math

days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

#•	Торта - 45 лв.
#•	Гофрета - 5.80 лв.
#•	Палачинка – 3.20 лв.

cakes_per_day = bakers * cakes
waffles_per_day = bakers * waffles
pancakes_per_day = bakers * pancakes
money_per_day = float((cakes_per_day * 45) + (waffles_per_day * 5.80) + (pancakes_per_day * 3.2))
total_money = money_per_day * days
expenses = total_money / 8 
charaty_money = total_money - expenses

print(f'{charaty_money:.2f}')
