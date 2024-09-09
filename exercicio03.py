#Processa os dados do usuário e realiza o cálculo do salário acresido de 10%

nome = input("Digite seu nome: ")
idade = int(input("Informe sua idade: "))
meses = idade * 12
salario = float(input("Informe seu salário: "))
salario = salario * 1.1

print(f"O salário acrescido de 10% de {nome}, que possui {idade} anos ({meses} meses), é de R${salario}")

