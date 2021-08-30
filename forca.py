import random

def jogar():
    inicializacao()

    palavra_secreta = escolha_palavra_secreta()
    letras_acertadas = espacos_palavra_secreta(palavra_secreta)

    acertou = False
    enforcou = False
    erros = 0

    tentativas_total = definindo_tentativas()

    imprime_tentativas_e_letras(tentativas_total, letras_acertadas)

    while (not acertou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            acerto_chute(chute, palavra_secreta, letras_acertadas)

        else:
            erros += 1
            tentativa_atual = tentativas_total - erros
            print("Você tem {} de {} tentativas".format(tentativa_atual, tentativas_total))

        enforcou = erros == tentativas_total
        acertou = "_" not in letras_acertadas
    if (acertou):
        imprime_ganhador()
    elif (enforcou):
        imprime_perdedor(palavra_secreta)

    imprime_fim_jogo()

def inicializacao():
    print("**********************************")
    print("   Bem vindo ao jogo da forca!!   ")
    print("**********************************")

def escolha_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = []

        for linha in arquivo:
            palavras.append(linha.strip().upper())

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta

def espacos_palavra_secreta(palavra):
    return ["_" for letra in palavra]

def escolha_nivel():
    print("Escolha a dificuldade: ", "(1) Fácil (2) Médio (3) Difícil", sep='\n')
    print("**********************************")
    nivel = int(input("Qual a dificuldade deseja? "))
    return nivel

def definindo_tentativas():
    nivel = 0
    cod_nivel = nivel != 1 and nivel != 2 and nivel != 3

    while (cod_nivel):
        nivel = escolha_nivel()
        if (nivel == 1):
            tentativas_total = 20
            break
        elif (nivel == 2):
            tentativas_total = 12
            break
        elif (nivel == 3):
            tentativas_total = 5
            break
        elif (nivel < 1 or nivel > 3):
            print("Código Inválido!")
            print("****************")
            continue
    return tentativas_total

def imprime_tentativas_e_letras(tentativas_total, letras_acertadas):
    print("Voce tem um total de {} tentativas".format(tentativas_total), "Boa sorte!", sep="\n")
    print("**********************************")
    print("A palavra tem {} letras".format(len(letras_acertadas)), letras_acertadas, sep="\n")
    print("**********************************")

def acerto_chute(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
    print(letras_acertadas)
    print("falta achar {} letras.".format(letras_acertadas.count("_")))

def imprime_ganhador():
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

def imprime_perdedor(palavra_secreta):
    print("Poxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_fim_jogo():
    print("**********************************")
    print("           Fim de jogo!")
    print("**********************************")

if(__name__ == "__main__"):
    jogar()


