#Receber um número do usuário e mostrar todos os números ímpares do intervalo de 1 até o número digitado.

numero = int(input("Informe o número desejado: "))

for i in range(1, numero + 1):
    if i % 2 != 0:
        print(i)




