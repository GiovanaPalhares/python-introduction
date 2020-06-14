n = int(input("Digite um valor: "))
lista = []
while n != 0:
    lista.append(n)
    n = int(input("Digite um valor: "))

if n == 0:
    lista.reverse()
    print(lista)


