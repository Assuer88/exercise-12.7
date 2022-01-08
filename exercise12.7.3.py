per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада:"))
for key in per_cent:
    per_cent[key] = per_cent[key] * money/100
x=(list(per_cent.values()))
deposit = [int(c) if isinstance(c, float) else c for c in x]
max_deposit=max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать:",max_deposit)
