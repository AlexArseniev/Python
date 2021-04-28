import math
budget = float(input())
ticket_type_input = input()
group_size = int(input())

ticket_type = ticket_type_input.lower()

# vip = 499.99 normal - 249.99
ticket_price = 0

if ticket_type == "vip":
    ticket_price = group_size * 499.99
elif ticket_type == "normal":
    ticket_price = group_size * 249.99

money_for_tickets = 0
travel_money = 0

if group_size <= 4:
    travel_money = budget * 0.75
elif group_size <= 9:
    travel_money = budget * 0.6
elif group_size <= 24:
    travel_money = budget * 0.5
elif group_size <= 49:
    travel_money = budget * 0.4
else:
    travel_money = budget * 0.25

money_for_tickets = budget - travel_money
difference = abs(money_for_tickets - ticket_price)
if money_for_tickets >= ticket_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
