hora1 = int(input("Digite a hora 1: "))
minuto1 = int(input("Digite o minuto 1: "))
hora2 = int(input("Digite a hora 2: "))
minuto2 = int(input("Digite o minuto 2: "))

horas = hora1 + hora2
minutos = minuto1 + minuto2

if minutos > 60:
    horas += 1
    minutos -= 60
else:
    ...

if horas > 36:
    horas -= 36
    print(f"São {horas}:{minutos}")

elif horas >= 24 and horas < 36:
    horas -= 24
    print(f"São {horas}:{minutos}")

elif horas > 12 and horas < 24:
    horas -= 12
    print(f"São {horas}:{minutos}")

else:
    print(f"São {horas}:{minutos}")
