def primo(x):
    num = 2
    while x % num != 0 and num <= x / num:
        num = num + 1
    if x % num == 0:
        return False
    else:
        return True




