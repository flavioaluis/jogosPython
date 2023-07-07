import random

def jogar():

    print('*********************************')
    print('Bem vindo ao jogo de Adivinhação!')
    print('*********************************')

    numeroSecreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 700

    print("Qual é o nível de dificuldade?")
    print("(1) Fácil - (2) Médio - (3) Difícil")

    nivel = int(input("Defina um nível: "))

    if (nivel == 1):
        tentativas = 12
    elif (nivel == 2):
        tentativas = 8 
    else:
        tentativas = 4 

    for rodada in range(1, tentativas + 1 ):
        print("Tentativa {} de {}" .format(rodada,tentativas))
        chuteS = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", (chuteS))
        chute = int(chuteS)

        if(chute < 1 or chute > 100 ):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numeroSecreto
        maior   = chute > numeroSecreto
        menor   = chute < numeroSecreto

        if (acertou):
                print("Você acertou! e fez {} pontos" .format(pontos))
                break
        else:
            if(maior):
                
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")

            perdidos = abs(numeroSecreto - chute)
            pontos = pontos - perdidos

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()


