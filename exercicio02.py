#Receba o nome e duas notas de um aluno, calcule e exiba a média dele.

nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2
print(f"A média do aluno {nome} é: {media}")