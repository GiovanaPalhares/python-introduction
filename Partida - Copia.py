n = "peças do jogo"
m = "limite para retirar"



def computador_escolhe_jogada(n, m, computador_remove=1):
    resto = n - computador_remove
    if computador_remove >= m:
        return m
    elif resto % (m + 1) == 0:
        return computador_remove
    else:
        computador_escolhe_jogada(n, m, computador_remove + 1)


computador_escolhe_jogada(10, 3)

def computador_escolhe_jogada(n, m):
    computador_remove = 1
    while computador_remove < m:
        resto = n - computador_remove
        if resto % (m + 1) == 0:
            break
        else:
            computador_remove += 1
    return computador_remove



def usuario_escolhe_jogada(n, m):
    usuario_remove = int(input("Quantas peças você vai tirar? "))
    print("")
    if 0 < usuario_remove <= m and usuario_remove <= n:
        print("você tirou", usuario_remove, "peças do tabuleiro")
        return usuario_remove
    else:
        print("jogada inválida! tente novamente")
        return usuario_escolhe_jogada(n, m)



def partida():
    isValidInput = False
    while not isValidInput:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        print("")

        isValidInput = m < n or n > 1
        if not isValidInput:
            print("valores inválidos! tente novamente")

    eh_a_vez_do_computador = n % (m + 1) == 0

    while n > 0:
        if eh_a_vez_do_computador:
            n -= computador_escolhe_jogada(n, m)
            eh_a_vez_do_computador = False
        else:
            n -= usuario_escolhe_jogada(n, m)
            eh_a_vez_do_computador = True





    if n % (m + 1) == 0:
        print("Computador começa!")
        print("o computador tirou", computador_escolhe_jogada(n, m), "peças do tabuleiro")
        print("agora temos", n, "peças no tabuleiro")
        while n > 0:
            print("você tirou", usuario_escolhe_jogada(n, m), "peças do tabuleiro")
            print("agora temos", n, "peças no tabuleiro")
            if n == 0:
                print("você venceu")
            elif n > 0:
                print("o computador tirou", computador_escolhe_jogada(n, m), "peças do tabuleiro")
                print("agora temos", n, "peças no tabuleiro")
                if n == 0:
                    print("computador venceu")
    else:
        print("Você começa!")
        usuario_escolhe_jogada(n,m)
        while n > 0:
            computador_escolhe_jogada(n,m)
            usuario_escolhe_jogada(n,m)



def main():
    print("Bem vindo ao jogo do NIM! Escolha: ")
    print("")
    print(" 1 - para uma partida isolada ")
    jogo = int(input(" 2 - para jogar um campeonato "))
    if jogo == 1:
        print("Voce escolheu jogar uma partida isolada")
        partida()
    else:
        if jogo == 2:
            print("Voce escolheu um campeonato")
            print("")
            campeonato()


def campeonato():
    print("**** RODADA 1 ****")
    partida()
    print("")
    print("**** RODADA 2 ****")
    partida()
    print("")
    print("**** RODADA 3 ****")
    partida()



main()

