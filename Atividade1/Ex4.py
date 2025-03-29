dias = int(input("Quantos dias o carro foi alugado? "))
km = int(input("Quantos quilômetros foram rodados? "))

custo_diario = 90
taxa_extra = 12

custo_total = dias * custo_diario

if km >100:
    km_adicionais = km - 100
    custo_total += km_adicionais * taxa_extra

print(f"O valor total a ser pago é: R${custo_total}")