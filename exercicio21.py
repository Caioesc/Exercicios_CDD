#Ler 10 valores, calcular e escrever a média aritmética desses valores lidos. (Usando While)

soma = 0
cont = 1

while cont <= 10:
    nota = int(input(f"Digite a {cont}º nota: "))
    soma += nota
    cont += 1
media = soma/10
print(f"A média aritmética é igual a {media}")



