import adivinhacao
import forca

def escolher_jogo():
    print("**********************************")
    print("*Escolha um dos jogos para jogar*!")
    print("**********************************")

    print("Escolha um dos jogos: ", "(1)Forca (2)Adivinhação", sep='\n')
    jogo= int(input("Qual jogo? "))

    if (jogo == 1):
        print("Iniciando Jogo da forca...")
        forca.jogar()
    elif (jogo == 2):
        print("Iniciando jogo de adivinhação...")
        adivinhacao.jogar()
    else:
        print("**********************************")
        print("     Código de jogo inválido!     ")
        print("**********************************")


if (__name__ == "__main__"):
    escolher_jogo()
