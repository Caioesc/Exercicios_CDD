"""Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive).
   Considere que o N será sempre maior que ZERO."""

numero = int(input("Informe um número: "))
cont = 1

while cont <= numero:
    print(cont)
    cont += 1