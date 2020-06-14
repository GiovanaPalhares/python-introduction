import re


def le_assinatura():
    print("Bem vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado: ")
    print("")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média de sentença: "))
    pal = float(input("Entre o tamanho médio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


as_b = le_assinatura()
wal_b = le_assinatura()[0]
ttr_b = le_assinatura()[1]
hlr_b = le_assinatura()[2]
sal_b = le_assinatura()[3]
sac_b = le_assinatura()[4]
pal_b = le_assinatura()[5]


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


def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    return frase.split()


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


def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] = freq[p] + 1
        else:
            freq[p] = 1

    return len(freq)


def calcula_assinatura(texto):
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

    print("Tamanho médio palavra: ", tam_medio_palavra(texto))

    def type_token(texto):
        lista = []
        for i in texto.split():
            lista.append(i)

        return n_palavras_diferentes(lista) / len(texto.split())

    print("Type token: ", type_token(texto))

    def hapax(texto):
        lista = []
        for i in texto.split():
            lista.append(i)

        return n_palavras_unicas(lista) / len(texto.split())

    print("Hapax:", hapax(texto))

    uma_sentenca = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, " \
                   "há um pequeno sol amarelo e esquecido."
    def tam_med_sentencas(uma_sentenca):
        def conta_caracter(uma_sentenca):
            lista = []
            for i in uma_sentenca.split():
                lista.append(len(i))
            soma = 0
            for i in lista:
                soma = soma + i
            return soma

        return conta_caracter(uma_sentenca) / len(separa_sentencas(texto))

    print("Tamanho médio da sentença: ", tam_med_sentencas(uma_sentenca))

    def complexidade_sentenca(texto):
        return len(separa_frases(texto)) / len(separa_sentencas(texto))

    print("Complexidade de sentença: ", complexidade_sentenca(texto))

    def tamanho_medio_frase(texto):
        def cont_frase(texto):
            lista = []
            for i in re.split(r'[,:;]+', texto):
                lista.append(i)
            cont = 0
            for i in lista:
                cont = cont + len(i)
            return cont

        return cont_frase(texto) / len(separa_frases(texto))

    print("Tamanho médio de frase: ", tamanho_medio_frase(texto))

    return [tam_medio_palavra(), type_token(), hapax(), tam_med_sentencas(), complexidade_sentenca(),
            tamanho_medio_frase()]


wal_a = calcula_assinatura()[0]
ttr_a = calcula_assinatura()[1]
hlr_a = calcula_assinatura()[2]
sal_a = calcula_assinatura()[3]
sac_a = calcula_assinatura()[4]
pal_a = calcula_assinatura()[5]


print(calcula_assinatura(texto))


def compara_assinatura(as_a, as_b):
    grau_de_similaridade = abs(wal_a - wal_b) + abs(ttr_a - ttr_b) + abs(hlr_a - hlr_b) + abs(sal_a - sal_b) \
                           + abs(sac_a - sac_b) + abs(sal_a - sal_b) / 6
    return grau_de_similaridade


def avalia_textos(textos, ass_cp):
    for i in textos:
        calcula_assinatura(textos)
        compara_assinatura(texto, ass_cp)
    menorSim = compara_assinatura(texto, ass_cp)[0]
    for i in compara_assinatura(texto, ass_cp):
        if i < menorSim:
            menorSim = i

    return menorSim






