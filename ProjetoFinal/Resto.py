def computador_escolhe_jogada(n, m):
    computador_remove = 1
    while computador_remove < m:
        resto = n - computador_remove
        if resto % (m + 1) == 0:
            break
        else:
            computador_remove += 1
    return computador_remove


print(computador_escolhe_jogada(2, 1))

