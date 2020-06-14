def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("")
    if n % (m + 1) == 0 and m < n:
        print("Computador começa!")
        computador_escolhe_jogada(n,m)
        print("o computador tirou", computador_remove, "peças do tabuleiro")
        print("agora temos", n, "peças no tabuleiro")
        while n > 0:
            usuario_escolhe_jogada(n,m)
            print("você tirou", usuario_remove, "peças do tabuleiro")
            print("agora temos", n, "peças no tabuleiro")
            if n == 0:
                print("você venceu")
            else:
                if n > 0:
                computador_escolhe_jogada(n,m)
                print("o computador tirou", computador_remove, "peças do tabuleiro")
                print("agora temos", n, "peças no tabuleiro")
                if n == 0:
                    print("computador venceu")
     else:
        if n % (m+1) != 0 and m < n:
            print("Você começa!")
            usuario_escolhe_jogada(n,m)
            while n > 0:
                computador_escolhe_jogada(n,m)
                usuario_escolhe_jogada(n,m)
        else:
            if m >= n or n <= 0:
                print("valores inválidos! tente novamente")
                partida()