nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print(f"Aluno aprovado com média {media}")
else:
    if media < 4:
        print(f"Aluno reprovado com média {media}")
    else:
        print(f"Aluno está de recuperação com média {media}")
