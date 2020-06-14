largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
var = 0
cont = 0

while var < 2:
    print(largura * "#")
    var = var + 1
    while cont < (altura - 2):
        novaLargura = largura - 4
        print("#", (novaLargura * " "), "#")
        cont = cont + 1




