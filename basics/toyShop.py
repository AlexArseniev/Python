vacation_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

money = (puzzle_count * 2.6) + (dolls_count * 3) + \
    (bears_count * 4.1) + (minions_count * 8.2) + (trucks_count * 2)

toys_total = puzzle_count + dolls_count + \
    bears_count + minions_count + trucks_count

if toys_total >= 50:
    money -= money * 0.25

money -= money * 0.1
money_left = abs(vacation_price - money)


if money >= vacation_price:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_left:.2f} lv needed.")
