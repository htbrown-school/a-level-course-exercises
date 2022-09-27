import locale, math
locale.setlocale(locale.LC_ALL, '')

pictures = int(input("How many picture messages will you send: "))
texts = int(input("How many text messages will you send: "))
data = int(input("How much data will you use (in MB): "))

cost = (pictures * 0.35) + (texts * 0.1) + (math.ceil(data / 500) * 2.5)
print(f"Your total for the month is {locale.currency(cost, '£')}")

if cost > 10:
    print("You would likely be better on a contract plan.")