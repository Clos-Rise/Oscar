revenue = 22_000_000_000
net_income = 6_500_000_000
assets = 110_300_000_000
net_assets = 106_005_000_000

revenue_change = 0.008
assets_change = 0.068
net_assets_change = 0.073
net_income_change = 0.034

revenue_per_minute = (revenue * (1 + revenue_change) / 52 / 4 / 7 / 24 / 60)

net_income_per_minute = (net_income * (1 + net_income_change) / 52 / 4 / 7 / 24 / 60)

assets_per_minute = (assets * (1 + assets_change) / 52 / 4 / 7 / 24 / 60)

net_assets_per_minute = (net_assets * (1 + net_assets_change) / 52 / 4 / 7 / 24 / 60)

print(f"Доход в минуту: {round(revenue_per_minute, 2)} rubles")
print(f"Чистый доход в минуту: {round(net_income_per_minute, 2)} rubles")
print(f"Активы в минуту: {round(assets_per_minute, 2)} rubles")
print(f"Чистые активы в минуту: {round(net_assets_per_minute, 2)} rubles")

#powered by Тифаней
#данные примерные , я вам тут не математик
