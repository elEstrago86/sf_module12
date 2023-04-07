# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Планируемая сумма вклада: "))

deposit = []

for bank, percent in per_cent.items():
    bank_deposit = round(money * percent / 100, 2)
    deposit.append(bank_deposit)

max_deposit = max(deposit) # находим максимальное значение в списке deposit

print("Сумма вклада: {}, накопленные средства: {}".format(money, deposit))
print("Максимальная сумма, которую вы можете заработать: {}".format(max_deposit))






















