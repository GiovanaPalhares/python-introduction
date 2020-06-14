def computador_escolhe_jogada(n, m, computador_remove=1):
    resto = n - computador_remove
    if computador_remove >= m:
        return m
    elif resto % (m + 1) == 0:
        return computador_remove
    else:
        computador_escolhe_jogada(n, m, computador_remove + 1)


computador_escolhe_jogada(10, 3)