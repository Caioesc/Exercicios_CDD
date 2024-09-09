#Receber 10 números do usuário e mostre a soma de todos os números ímpares.

soma = 0
for i in range(10):
    numero = int(input("Digite o número desejado: "))
    if numero % 2 != 0:
        soma += numero
print(f"A soma total dos valores ímpares é de: {soma}")