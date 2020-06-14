import re


def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i = i + 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == "":
        del sentencas[-1]
    return sentencas


n_total_sentencas = len(separa_sentencas(texto))


#print(separa_sentencas(le_textos()[1]))

textos = le_textos()

#i = 1
#b = 0
#while i > 0:
 #       texto + int(i) = le_textos()[b]
  #      i = i + 1
   #     b = b + 1


def auxiliar_separa(textos):
    texto1 = 0
    for i in textos:
        texto1 = i
        print(texto1)


print(auxiliar_separa(textos))




#print(separa_sentencas(le_textos()[0]))
