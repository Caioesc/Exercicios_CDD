""" Problema: Receba do usuário uum número de 1 a 12 e mostre o nome do mês correspondente.
    Caso o mês não exista, mostrar "Valor inválido"  *Use If, Elif e Else*"""

mes = int(input("Informe o número do mês que você deseja: "))

if mes < 1 or mes > 12:
    print("Valor inválido")
elif mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
