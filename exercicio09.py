""" Receba a quantidade de litros abastecidos, depois o tipo de combustível e no final
    exiba o valor total de acordo com o combustível (G - Gasolina - R$ 5.80/ E - Etanol - R$4.90)"""

litros = float(input("Informe quantos litros foram abastecidos: "))
comb = input("Informe o tipo de combustível (Digite E para etanol e G para gasolina): ")
preco = 0

if comb == "E" or comb == "e":
    preco = litros * 4.90
    print(f"O valor total foi de R${preco: .2f}")
else:
    if comb == "G" or comb == "g":
        preco = litros * 5.80
        print(f"O valor total foi de R${preco: .2f}")
    else:
        print("Tipo de combustível inválido!")
