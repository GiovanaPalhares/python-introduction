temperaturasMes = [24, 23, 22, 21, 21, 20, 19, 23, 21, 10, 20, 20, 18, 32, 17, 20, 50]

maiorTemp = 0

for i in temperaturasMes:
    if i > maiorTemp:
        maiorTemp = i


menorTemp = maiorTemp

for i in temperaturasMes:
    if i < menorTemp:
        menorTemp = i


print("A maior temperatura dos últimos dias foi:", maiorTemp, "C")
print("A menor temperatura dos últimos dias foi:", menorTemp, "C")

def teste(maiorTemp):
    if maiorTemp != 50:
        print("Erro")

teste(maiorTemp)
