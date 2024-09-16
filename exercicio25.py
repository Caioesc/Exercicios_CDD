"""Faça um código para ler a senha de um usuário e após 3 tentativas erradas, sair do programa, informando que a
   senha está bloqueada. OBS: A cada tentativa errada, o programa deve mostrar as tentativas restantes."""

pin = 1234
senha = int(input("Digite sua senha: "))
tentativas = 1

while senha != pin and tentativas < 3:
    senha = int(input(f"Senha incorreta, você tem {3 - tentativas} tentativas restantes. \nDigite novamente:  "))
    tentativas += 1

if tentativas == 3 and senha != pin:
    print("Número máximo de tentativas alcançadas, senha bloqueada!")
else:
    print("Acesso concedido! \nSaldo: R$50.000")



