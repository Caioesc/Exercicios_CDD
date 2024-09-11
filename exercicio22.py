"""Faça um código que receba o número de alunos de uma sala de aula e depois solicite as notas desses alunos,
no final, mostre a média aritmética da turma."""

repetir = 1

while repetir != 2:
    alunos = int(input("Informe a quantidade de alunos: "))
    cont = 1
    soma = 0
    a = 0
    repetir = 1
    while cont < alunos + 1:
        notas = float(input(f"Informe a nota do {cont}º aluno: "))
        soma += notas
        cont += 1
    media = soma/alunos
    print(f"A média aritmética da turma é: {media}")
    repetir = int(input("\nDeseja fazer novamente? \n 1 - Sim \n 2 - Não"))

print("\nOperação encerrada!")
