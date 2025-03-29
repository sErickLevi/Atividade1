segundos = int(input("Digite um valor em segundos: "))

dias = segundos // 86400
segundos_restantes = segundos % 86400
horas = segundos_restantes // 3600
segundos_restantes %= 3600
minutos = segundos_restantes // 60
segundos_restantes %= 60

# Exibe o resultado
print(f"{segundos} segundos equivalem a um total de:")
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")