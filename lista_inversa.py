num = 1
lista = []
while num != 0:
    num = int(input("Digite um valor: "))
    lista.append(num)
lista.reverse()
del lista[0]
len(lista)
for i in lista:
    print(i)






