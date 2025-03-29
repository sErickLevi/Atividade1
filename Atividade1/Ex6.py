def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def gerar_primos(contagem):
    primos = []
    n = 2
    while len(primos) < contagem:
        if verificar_primo(n):
            primos.append(n)
        n += 1
    return primos

primos = gerar_primos(100)
print(primos)