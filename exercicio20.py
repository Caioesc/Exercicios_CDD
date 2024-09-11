"""Ler 10 valores e escrever quantos desses valores lidos estão no intervalo de [10,20]
(incluindo os valores 10 e 20 no intervalo) e quantos deles estão fora do intervalo.
OBS: USE APENAS UM IF, UMA VARIÁVEL PARA CONTAR E APENAS UM PRINT"""

dentro = 0
for i in range (1, 11):
    numero = int(input(f"Digite o {i}º número: "))
    if 10 <= numero <= 20:
        dentro += 1

print(f"A quantidade de números dentro do intervalo é de: {dentro} e fora é {10 - dentro}")

