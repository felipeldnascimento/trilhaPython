print("***************************************")
print("*** Bem vindo ao jogo da advinhação ***")
print("***************************************")

numero_secreto = 42

chute = input("Digite um número: ")

print("Você digitou: ", chute)

chute = int(chute)

acertou  = chute == numero_secreto
maior    = chute > numero_secreto
menor    = chute < numero_secreto and chute > 0
negativo = chute < numero_secreto and chute < 0

if(acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou. Número acima do número secreto.")
    if(menor):
        print("Você errou. O número inserido é positivo e abaixo do número secreto.")
    elif(negativo):
        print("Você errou. O número inserido é negativo e abaixo do número secreto.")

print("Fim do jogo.")