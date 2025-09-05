exchange_rate = float(input("Please input the current exchange rate for the Euro to the Dollar. Please leave off any monetary symbols. Enter rate here: "))
amount = float(input("Please input the amount of currency that you would like to exchange: "))

total = amount * exchange_rate
result = total - 3

print(result)
