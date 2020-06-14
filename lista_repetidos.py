lista = [2,3,4,5,2,3,67,8]

def remove_repetidos(lista):
    lista1 = []
    for i in lista:
        if i not in lista1:
            lista1.append(i)
    lista1.sort()
    print(lista1)
    return lista1


remove_repetidos(lista)



