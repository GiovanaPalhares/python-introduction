n = "peças do jogo"
m = "limite para retirar"





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
        print("Você tirou", usuario_remove, "peças.")
        return usuario_remove
    else:
        print(" Oops ! Jogada inválida! tente de novo.")
        return usuario_escolhe_jogada(n, m)



def partida():
    isValidInput = False
    while not isValidInput:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        print("")

        isValidInput = m < n and n > 1
        if not isValidInput:
            print("valores inválidos! tente novamente")

    eh_a_vez_do_computador = n % (m + 1) != 0

    if eh_a_vez_do_computador:
        print("Computador começa!")
        print("")
    else:
        print("Você começa!")
        print("")


    while n > 0:
        if eh_a_vez_do_computador:
            print("o computador tirou", computador_escolhe_jogada(n, m), "peças.")
            n -= computador_escolhe_jogada(n, m)
            print("agora temos", n, "peças.")
            print("")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
            eh_a_vez_do_computador = False
        else:
            n -= usuario_escolhe_jogada(n, m)
            print("Agora temos", n, "peças.")
            print("")
            if n == 0:
                print("você venceu")
            eh_a_vez_do_computador = True


def main():
    print("Bem vindo ao jogo do NIM! Escolha: ")
    print("")
    print(" 1 - para jogar uma partida isolada ")
    jogo = int(input(" 2 - para jogar um campeonato "))
    print("")
    if jogo == 1:
        print("Voce escolheu jogar uma partida isolada!")
        partida()
    else:
        if jogo == 2:
            print("Voce escolheu um campeonato!")
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
    print("")
    print("**** Final do campeonato! **** ")
    print("Placar: Você 0 x 3 Computador")



main()

