import re
from statistics import mean


def le_assinatura():
    """A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os
    textos fornecidos """
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento"""
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    """A funcao recebe um texto e devolve uma lista das sentencas dentro do texto"""
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca"""
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    """A funcao recebe uma frase e devolve uma lista das palavras dentro da frase"""
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez"""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas"""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def tamanho_das_palavras(frase):
    palavras = separa_palavras(frase)

    tamanhos = []
    for palavra in palavras:
        tamanhos.append(len(palavra))

    return tamanhos


def tam_medio_das_palavras_no_texto(texto):
    sentencas = separa_sentencas(texto)

    tamanhos = []
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            tamanhos.extend(tamanho_das_palavras(frase))

    return mean(tamanhos)


def lista_de_palavras(texto):
    sentencas = separa_sentencas(texto)

    lista_palavras = []
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras = separa_palavras(frase)
            lista_palavras.extend(palavras)

    return lista_palavras


def type_token(texto):
    palavras = lista_de_palavras(texto)
    return n_palavras_diferentes(palavras) / len(palavras)


def hapax_legomana(texto):
    palavras = lista_de_palavras(texto)
    return n_palavras_unicas(palavras) / len(palavras)


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
    for traco in range(0, len(as_a)):
        grau_similaridade += (abs(as_a[traco] - as_b[traco]))

    return grau_similaridade / len(as_a)


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do
     texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    comparacoes = []
    for texto in textos:
        assinatura_texto = calcula_assinatura(texto)
        comparacoes.append(compara_assinatura(assinatura_texto, ass_cp))

    minimo_comparacao = min(comparacoes)
    for index in range(0, len(comparacoes)):
        if comparacoes[index] == minimo_comparacao:
            return index + 1


def main():
    assinatura = le_assinatura()
    textos = le_textos()
    resultado = avalia_textos(textos, assinatura)
    print("O autor do texto {} está infectado com COH-PIAH".format(resultado))


main()
