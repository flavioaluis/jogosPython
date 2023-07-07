import random

def jogar():

    imprimeAbertura()
    palavraSecreta = bancoPalavras()
    letrasAcertadas = iniciarLetras(palavraSecreta)
    
    enforcou = False
    acertou = False 
    erros = 0

    print(letrasAcertadas)

    while(not enforcou and not acertou):

        chute = pedeChute()
        
        if(chute in palavraSecreta):
            marcarCorreto(chute,letrasAcertadas, palavraSecreta)
        else:
            erros += 1
            desenhaForca(erros)
        
        enforcou = erros == 7
        
        acertou = "_" not in letrasAcertadas
        print(letrasAcertadas)
    if(acertou):
        imprimeVencedor()
    else:
        imprimePerdedor()







def imprimeAbertura():
    print('*************************************')
    print('*****Bem vindo ao jogo de Forca!*****')
    print('*************************************')

def iniciarLetras(palavra):
    return ["_" for letra in palavra]

def pedeChute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marcarCorreto(chute,letrasAcertadas,palavraSecreta):
    posicao = 0
    for letra in palavraSecreta:
        if (chute == letra):
            letrasAcertadas[posicao] = letra
        posicao += 1

def bancoPalavras():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavraSecreta = palavras[numero].upper()
    return palavraSecreta

def imprimeVencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprimePerdedor():
    print("Você perdeu!")


if(__name__=="__main__"):
    jogar()
