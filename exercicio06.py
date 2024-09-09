#Receba dois números e os exiba em ordem crescente.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 < n2:
    print(n1, n2)
else:
    if n2 < n1:
        print(n2, n1)
    else:
        print("São iguais.")