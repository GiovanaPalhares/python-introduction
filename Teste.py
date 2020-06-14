def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat


n = int(input("Digite o valor de n: "))
print(fatorial(n))

k = int(input("Digite o valor de k: "))


def binomial(n,k):
    return fatorial(n) / (fatorial(k) * (fatorial(n-k)))


print("O binomial de n e k eh", binomial(n,k))

def teste():
    if fatorial(1) == 1:
        print(Correto)
    else:
        print(Incorreto)

