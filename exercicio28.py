#Informar 2 numeros, escolher a operação ou comando desejado.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

escolha = 0

while escolha != 6:
    escolha = int(input("\nDigite a opção desejada. \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Digitar novo número \n6 - Sair"))
    if escolha == 1:
        resultado = numero1 + numero2
        print(f"{numero1}+{numero2} = {resultado}")
        escolha = 6
    elif escolha == 2:
        resultado = numero1 - numero2
        print(f"{numero1}-{numero2} = {resultado}")
        escolha = 6
    elif escolha == 3:
        resultado = numero1 * numero2
        print(f"{numero1}x{numero2} = {resultado}")
        escolha = 6
    elif escolha == 4:
        resultado = numero1 / numero2
        print(f"{numero1}/{numero2} = {resultado}")
        escolha = 6
    elif escolha == 5:
        novo_numero = int(input("\nQual número você deseja trocar? \n1 - Primeiro \n2 - Segundo \n3 - Ambos"))
        if novo_numero == 1:
            numero1 = int(input("Digite o novo valor para o primeiro número: "))
        elif novo_numero == 2:
            numero2 = int(input("Digite o novo valor para o segundo número: "))
        elif novo_numero == 3:
            numero1 = int(input("Digite o novo valor para o primeiro número: "))
            numero2 = int(input("Digite o novo valor para o segundo número: "))

    elif escolha == 6:
        print("Programa encerrado!")
    else:
        print("Digite uma opção válida!")


