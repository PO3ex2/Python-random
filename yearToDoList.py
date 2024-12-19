import datetime
dateTimeNow = datetime.datetime.now()
year = dateTimeNow.strftime("%Y")

mission1 = input("Zadejte svůj první cíl: ")
mission2 = input("Zadejte svůj druhý cíl: ")
mission3 = input("Zadejte svůj třetí cíl: ")

print(f"V roce {year} chci dosáhnout těchto cílů:")
print(f"1. {mission1}")
print(f"2. {mission2}")
print(f"3. {mission3}")