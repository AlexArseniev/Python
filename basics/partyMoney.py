whisky_price = float(input())
beer_liters = float(input())
wine_liters = float(input())
raki_liters = float(input())
whisky_liters = float(input())

raki_price = whisky_price / 2
wine_price = raki_price - (raki_price * 0.4)
beer_price = raki_price - (raki_price * 0.8)

money_needed = (whisky_liters * whisky_price) + (beer_liters * beer_price) + (raki_price * raki_liters) + (wine_liters * wine_price)

print(f'{money_needed:.2f}')
