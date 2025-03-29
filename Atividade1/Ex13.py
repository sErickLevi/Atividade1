salario_inicial = int(input("Digite o salário inicial: "))
aumento_percentual = int(input("Digite o aumento percentual inicial: "))
anos = int(input("Digite o número de anos: "))

salario_final = salario_inicial
for i in range(anos):
    salario_final += salario_final * (aumento_percentual / 100)
    aumento_percentual *= 2  
 
print(f"O salário após {anos} anos será: R${salario_final}")