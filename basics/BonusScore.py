number = int(input())
result = number
bonus_points = 0

if number <= 100:
    result += 5
    bonus_points += 5
elif number <= 1000:
    result += number * 0.2
    bonus_points += number * 0.2
else:
    result += number * 0.1
    bonus_points += number * 0.1

if number % 2 == 0:
    result += 1
    bonus_points += 1
elif number % 5 == 0:
    result += 2
    bonus_points += 2

print(bonus_points)
print(result)
