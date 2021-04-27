dogs_count = int(input())
other_pets_count = int(input())

dog_food_money = float(dogs_count * 2.5)
other_pets_money = other_pets_count * 4

total_money = float(dog_food_money + other_pets_money)

print(f'{total_money:.2f} lv.')
