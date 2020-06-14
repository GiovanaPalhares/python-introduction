
def primo(x):
    num = 2
    while x % num != 0 and num <= x / num:
        num = num + 1
    if x % num == 0:
        return False
    else:
        return True


def maior_primo(x):
    if primo(x):
        return(x)
    else:
        while x > 2:
            i = 1
            if primo(x-i):
                return (x-i)
            i = i + 1


(maior_primo(20))















