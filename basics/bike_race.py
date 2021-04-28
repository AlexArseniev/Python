young_bikers = int(input())
veteran_bikers = int(input())
track_type_input = input()

track_type = track_type_input.lower()

young_bikers_money = 0
veteran_bikers_money = 0

if track_type == "trail":
    young_bikers_money = young_bikers * 5.5
    veteran_bikers_money = veteran_bikers * 7
elif track_type == "cross-country":
    if (young_bikers + veteran_bikers) >= 50:
        young_bikers_money = young_bikers * (8 - (8 * 0.25))
        veteran_bikers_money = veteran_bikers * (9.5 - (9.5 * 0.25))
    else:
        young_bikers_money = young_bikers * 8
        veteran_bikers_money = veteran_bikers * 9.5
elif track_type == "downhill":
    young_bikers_money = young_bikers * 12.25
    veteran_bikers_money = veteran_bikers * 13.75
else:
    young_bikers_money = young_bikers * 20
    veteran_bikers_money = veteran_bikers * 21.50

total = young_bikers_money + veteran_bikers_money

total -= total * 0.05

print(f"{total:.2f}")
