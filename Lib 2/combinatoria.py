def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def coef_binomial_analitico(n, k):
    if k < 0 or k > n:
        return 0
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

def coef_binomial_recursivo(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return coef_binomial_recursivo(n - 1, k) + coef_binomial_recursivo(n - 1, k - 1)
