# Teste de primalidade

def eh_primo(n): # força bruta
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def eh_primo_otimizado(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Inverso modular

def mdc_extendido(a, b):
    if b == 0:
        return a, 1, 0 
    mdc, x1, y1 = mdc_extendido(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return mdc, x, y

def inverso_modular(a, m):
    mdc, x, _ = mdc_extendido(a, m)
    if mdc != 1:
        return None 
    return x % m
