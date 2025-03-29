nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média aritmética simples: {media}")

mediaponderada1 = (nota1 * 2 + nota2 * 2 + nota3 * 3) / (2 + 2 + 3)

print(f"Média ponderada (pesos 2, 2, 3): {mediaponderada1}")

mediaponderada2 = (nota1 * 1 + nota2 * 2 + nota3 * 2) / (1 + 2 + 2)

print(f"Média ponderada (pesos 1, 2, 2): {mediaponderada2}")