"""Faça um código para ler 2 valores e realize a divisão do primeiro pelo segundo valor recebido, caso o segundo
   valor digitado, seja 0, solicite novamente o valor, informando que só aceitaremos valores diferentes de zero"""


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

while numero2 == 0:
    numero2 = int(input("\nO segundo valor não pode ser 0! Digite o segundo número novamente: "))

resultado = numero1/numero2
print(f"\nO resultado da divisão é {resultado}")





