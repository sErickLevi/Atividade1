numero = int(input("Digite um número ímpar: "))

if numero % 2 == 0:
    print("O número digitado não é ímpar.")
else:
    numero_anterior = numero - 2
    numero_proximo = numero + 2

    diferenca = (numero_proximo ** 2) - (numero_anterior ** 2)

    print(f"A diferença entre o quadrado do próximo número ímpar ({numero_proximo}) e do anterior ({numero_anterior}) é: {diferenca}")