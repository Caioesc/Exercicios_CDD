#Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma total dos 10 números lidos.

soma = 0
for i in range(0, 10):
    numero = int(input("Informe um número para a soma: "))
    soma += numero

print(f"A soma total dos valores é: {soma}")