import random

def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de adivinhação!!")
    print("**********************************")

    print("Nesse jogo vc deve descobrir qual é o numero secreto",  "Boa sorte!!", sep="\n")
    print("**********************************")

    num_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000
    nivel = 0
    cod_nivel = nivel != 1 and nivel != 2 and nivel != 3

    print("Escolha a dificuldade: ", "(1) Fácil (2) Médio (3) Difícil", sep='\n')
    print("**********************************")


    while (cod_nivel):

        nivel = int(input("Qual a dificuldade deseja? "))
        if (nivel == 1):
            tentativas = 20
            break
        elif (nivel == 2):
            tentativas = 10
            break
        elif (nivel == 3):
            tentativas = 5
            break
        elif (nivel < 1 or nivel > 3):
            print("Código Inválido!")
            print("****************")
            continue


    print("**********************************")
    print ("Sua pontuação inicial é de ", pontos)
    print("**********************************")

    for rodada in range(1, tentativas+1):

        print("Tentativa {} de {}".format(rodada, tentativas))

        chute = int(input("Digite um numero de 1 a 100: "))

        if (chute < 1 or chute > 100):
            print("Número inválido!")
            continue

        acertou = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto

        if (acertou):
            print ("Você acertou!", "Você ganhou {} pontos".format(pontos), sep= '\n')
            break
        elif(maior):
            print (" O numero que digitou é maior que o numero secreto")
        elif(menor):
            print(" O numero que digitou é menor que o numero secreto")


        pontuacao_perdida= abs(num_secreto - chute)
        pontos -= pontuacao_perdida




    print("**********************************")
    print("           Fim de jogo!")
    print("**********************************")

if (__name__ == "__main__"):
    jogar()





