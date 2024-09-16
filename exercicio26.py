"""Escreva um código para ler as notas de 1a. e 2a. avaliações de um aluno, calcule e imprima a média desse aluno.
   Só devem ser aceitos valores válidos, durante a leitura, (0 a 10) para cada nota. Implemente a função caso o usuário deseje repetir"""
repetir = 1

while repetir == 1:
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Digite uma nota válida: "))

    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Digite uma nota válida: "))

    media = (nota1 + nota2)/2
    print(f"A média do aluno é igual a {media:.2f}")

    repetir = int(input("Deseja repetir? \n1 - Sim \n2 - Não"))

