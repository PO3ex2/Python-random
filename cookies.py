cookieTypeAmount = int(input("Zadejte počet druhu cukroví: "))

timeNeeded = 0

cookieTypeController = 1

while cookieTypeAmount != 0 :
    cookieType = cookieTypeAmount - (cookieTypeAmount-cookieTypeController)
    cookieTypeTime = int(input(f"Kolik je potřeba času na {cookieType}. typ sušenek: "))
    timeNeeded += cookieTypeTime
    cookieTypeAmount -= 1
    cookieTypeController += 1

print(timeNeeded)