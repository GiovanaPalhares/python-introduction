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
    usuario_escolhe_jogada(n, m)
    while n > 0:
        computador_escolhe_jogada(n, m)
        usuario_escolhe_jogada(n, m)