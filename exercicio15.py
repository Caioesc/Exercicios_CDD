"""Ler uma variável de número inteiro e mostrar a tabuada de multiplicação desse número (1-10)
   Formato da saída: 1 x 5 = 5; 2 x 5 = 10; etc..."""

numero = int(input("Digite o número desejado: "))
for i in range (1, 11):
    tabuada = i * numero
    print(f"{i} x {numero} = {tabuada}")
