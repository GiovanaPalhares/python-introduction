import re
texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol" \
        " amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, " \
        "há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, " \
        "são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."

#CALCULA ASSINATURA

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] = freq[p] + 1
        else:
            freq[p] = 1

    return len(freq)


def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == "":
        del sentencas[-1]
    return sentencas

separa_sentencas(texto)



def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas = unicas - 1
            freq[p] = freq[p] + 1
        else:
            freq[p] = 1
            unicas = unicas + 1

    return unicas



def tam_medio_palavra(texto):
    def conta_caracter(texto):
        lista = []
        for i in texto.split():
            lista.append(len(i))
        soma = 0
        for i in lista:
            soma = soma + i
        return soma

    return conta_caracter(texto) / len(texto.split())

print(tam_medio_palavra(texto))



def type_token(texto):
    lista = []
    for i in texto.split():
        lista.append(i)

    return n_palavras_diferentes(lista) / len(texto.split())

print(type_token(texto))


def hapax(texto):
    lista = []
    for i in texto.split():
        lista.append(i)

    return n_palavras_unicas(lista) / len(texto.split())

print(hapax(texto))


def tam_med_sentencas(sentencas):
    separa_sentencas(texto)

    def conta_caracter(sentencas):
        lista = []
        for i in sentencas.split():
            lista.append(len(i))
        soma = 0
        for i in lista:
            soma = soma + i
        return soma

    return conta_caracter(sentencas) / len(sentencas)


print(tam_med_sentencas(sentencas))







    def n_palavras_diferentes(lista_palavras):
        freq = dict()
        for palavra in lista_palavras:
            p = palavra.lower()
            if p in freq:
                freq[p] = freq[p] + 1
            else:
                freq[p] = 1

        return len(freq)

    def n_palavras_unicas(lista_palavras):
        freq = dict()
        unicas = 0
        for palavra in lista_palavras:
            p = palavra.lower()
            if p in freq:
                if freq[p] == 1:
                    unicas = unicas - 1
                freq[p] = freq[p] + 1
            else:
                freq[p] = 1
                unicas = unicas + 1

        return unicas