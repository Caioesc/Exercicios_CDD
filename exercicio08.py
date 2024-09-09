#Faça um algoritmo receba a quantidade de gols de dois times e exiba o time vencedor.

time1 = input("Digite o nome do primeiro time: ")
goltime1 = int(input(f"Informe quantos gols o {time1} fez: "))
time2 = input("Digite o nome do segundo time: ")
goltime2 = int(input(f"Informe quantos gols o {time2} fez: "))

if goltime1 > goltime2:
    print(f"O {time1} venceu por {goltime1} a {goltime2}")
else:
    if goltime2 > goltime1:
        print(f"O {time2} venceu por {goltime2} a {goltime1}")
    else:
        print("O jogo foi para os pênaltis!")
        p1 = int(input(f"Digite quantos gols o {time1} fez nos pênaltis: "))
        p2 = int(input(f"Digite quantos gols o {time2} fez nos pênaltis: "))
        if p1 > p2:
            print(f"{time1} venceu os pênaltis por {p1} a {p2}")
        else:
            print(f"{time2} venceu os pênaltis por {p2} a {p1}")




