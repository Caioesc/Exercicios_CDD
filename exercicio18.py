"""Ler o número de alunos existentes em uma turma e, após isto, ler as notas destes alunos, calcular e
   escrever a média aritmética dessas notas lidas."""

soma = 0
alunos = int(input("Digite o número de alunos: "))
for i in range(1, alunos+1):
    notas = int(input(f"Digite a nota do aluno {i}: "))
    soma += notas
media = soma/alunos
print(f"A média das notas dos alunos é: {media}")
