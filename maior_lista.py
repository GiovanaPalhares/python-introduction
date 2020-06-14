lista = [23, 32432, 23423]

def maior_elemento(lista):
    num = 0
    for i in lista:
        if i > num:
            num = i
    print(num)
    return num



maior_elemento(lista)



