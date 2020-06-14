print("**** Rodada 1 ****")

n = int(input("Quantas peças? "))
m = int(input("Limite de peças por jogada? "))

if n % (m + 1) == 0:
    print("Você começa")
else:
    print("Computador começa")


def computador_escolhe_jogada(n,m):
    x = 1
    if x % (m + 1) == 0:
        return x
    print("O computador tirou uma peça")


computador_escolhe_jogada(n,m)

print("Agora restam", n - 1, "peças no tabuleiro")




