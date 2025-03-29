quantidade_turmas = int(input("Digite a quantidade de turmas: "))

total_alunos = 0
turmas_com_mais_de_40 = 0

for i in range(1, quantidade_turmas + 1):
    alunos_na_turma = int(input(f"Digite a quantidade de alunos na turma {i}: "))
    if alunos_na_turma > 40:
        print(f"Atenção: A turma {i} tem mais de 40 alunos!")
        turmas_com_mais_de_40 += 1
    total_alunos += alunos_na_turma

media_alunos = total_alunos / quantidade_turmas

print(f"A média de alunos por turma é: {media_alunos}")
if turmas_com_mais_de_40 > 0:
    print(f"Existem {turmas_com_mais_de_40} turma(s) com mais de 40 alunos.")