years1 = int(input("Years:"))
print("number of exhibits:", years1*60*8*365 / 5)

exhibits = int(input("number of exhibits:"))

exhibits_minuts = exhibits * 5

days = exhibits_minuts / 480
exhibits_minuts -= days * 480

years2 = days // 365
days %= 365

print("you need-", "years=", years2, "days=", days, "mins=", exhibits_minuts)
