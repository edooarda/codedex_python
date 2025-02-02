pesos = int(input("How much do you have in Pesos? "))
soles = int(input("How much do you have in Soles? "))
reais = int(input("How much do you have in Reais? "))

total = (pesos * 0.00024) + (soles * 0.27) + (reais * 0.17)

print("Your amount in Dolar is: ", total)