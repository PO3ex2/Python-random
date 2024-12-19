treeHeight = int(input("Zadejte výšku stromu(použijte jen cela čísla): "))

baubleAmount = 0
baubleOnLayer = 1

while treeHeight != 0 :
    baubleAmount += baubleOnLayer
    baubleOnLayer *=2
    treeHeight -= 1
    
print(f"Na Vánočním stromečku je {baubleAmount} ozdob(a).") 




