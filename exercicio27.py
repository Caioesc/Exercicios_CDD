"""Problema: Entrada: 5 /// Sáida: 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 """

"""numero = int(input("Digite um número: "))

for y in range(1, numero + 1):
    for x in range(y):
        print(y, end = " ")"""

"""Entrada: 3 /// Saída: 1
                         22
                         333"""

"""numero = int(input("Digite um número: "))

for y in range(1, numero + 1):
    for x in range(y):
        print(y, end = " ")
    print("")"""

"""Saída: 0
          0 1
          0 1 2"""

numero = int(input("Digite um número: "))

for y in range(0, numero + 1):
    for x in range(y):
        print(x, end = " ")
    print("")



