from Functions import *
from statistics import mean


def tam_medio_das_palavras(frase):
    palavras = separa_palavras(frase)

    tamanhos = []
    for palavra in palavras:
        tamanhos.append(len(palavra))

    return mean(tamanhos)


def tam_medio_das_palavras_no_texto(texto):
    sentencas = separa_sentencas(texto)

    tamanhos = []
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            tamanho = tam_medio_das_palavras(frase)
            tamanhos.append(tamanho)

    return mean(tamanhos)


def numero_total_de_palavras_do_texto(texto):
    return len(texto.split())


def lista_de_palavras(texto):
    sentencas = separa_sentencas(texto)
    palavras_frase = 0
    lista_palavras = []
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras = separa_palavras(frase)
            for palavra in palavras:
                lista_palavras.append(palavra)
                palavras_frase = lista_palavras

    return palavras_frase


def type_token(texto):
    lista_de_palavras1 = lista_de_palavras(texto)
    return n_palavras_diferentes(lista_de_palavras1) / numero_total_de_palavras_do_texto(texto)


def hapax_legomana(texto):
    return n_palavras_unicas(lista_de_palavras(texto)) / numero_total_de_palavras_do_texto(texto)


def tamanho_medio_sentenca(texto):
    # a conta tá dando errada
    sentencas = separa_sentencas(texto)
    tamanho_sentenca = []
    for sentenca in sentencas:
        tamanho_sentenca.append(len(sentenca))

    return mean(tamanho_sentenca)


def complexidade_de_sentenca(texto):
    # numero total de frases dividido pelo numero de sentencas
    conta_frases = 0
    conta_sentencas = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        conta_sentencas += 1
        frases = separa_frases(sentenca)
        for frase in frases:
            conta_frases += 1
    numero_de_frases = conta_frases
    numero_de_sentencas = conta_sentencas

    return numero_de_frases / numero_de_sentencas


def tamanho_medio_de_frase(texto):
    # soma do número de caracteres em cada frase dividida pelo número de frases no texto
    numero_de_caracteres_frase = []
    numero_de_frases = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            numero_de_frases += 1
            numero_de_caracteres_frase.append(len(frase))

    return mean(numero_de_caracteres_frase)


def calcula_assinatura(texto):
    return [tam_medio_das_palavras_no_texto(texto), type_token(texto), hapax_legomana(texto),
            tamanho_medio_sentenca(texto), complexidade_de_sentenca(texto), tamanho_medio_de_frase(texto)]


def compara_assinatura(as_a, as_b):
    grau_similaridade = 0
    for traco in range(0, 6):
        grau_similaridade = grau_similaridade + (abs(as_a[traco] - as_b[traco]))

    return grau_similaridade / 6


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do
     texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    comparacao = []
    for texto in textos:
        assinatura_texto = calcula_assinatura(texto)
        comparacao.append(compara_assinatura(assinatura_texto, ass_cp))
    menor = comparacao[0]
    for similaridade in range(1, len(comparacao)):
        if comparacao[similaridade] < menor:
            menor = comparacao[similaridade]

    return menor


def main():
    assinatura = le_assinatura()
    textos = le_textos()
    resultado = avalia_textos(textos, assinatura)
    print("O autor do texto {} está infectado com COH-PIAH".format(resultado))
    

main()
