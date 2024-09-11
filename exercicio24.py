"""Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive).
   Considere que o N será sempre maior que ZERO."""

repetir = 1

while repetir != 2:
    numero = int(input("Informe um número: "))
    cont = 1
    repetir = 1
    while cont <= numero:
        print(cont)
        cont += 1
    repetir = int(input("\nDeseja fazer novamente? \n 1 - Sim \n 2 - Não"))
print("Operação encerrada!")