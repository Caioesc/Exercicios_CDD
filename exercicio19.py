#Ler 10 valores e escrever quantos desse valores lidos são NEGATIVOS.

negativos = 0
for i in range (1, 11):
    numero = int(input(f"Digite o {i}º número: "))
    if numero < 0:
        negativos += 1
print(f"A quantidade de números negativos é de: {negativos}")
