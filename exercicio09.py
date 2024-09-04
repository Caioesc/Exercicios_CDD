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
