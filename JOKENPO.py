# Grupo:
# João Vitor Gregorini
# João Victor Ribeiro Basso
# Bruno Renan Guttervill
# Giovanni Lucca Uchôa
# Guilherme Lopes Cruz
#JOKENPO

#VARIAVEIS

import random
p1 = -1
p2 = -1
pont_p1 = 0
pont_p2 = 0
modo = 0
range1 = range(0,4)
#TELA INICIAL

print('------------------------------------------')
print('----------------JOKEN PO------------------')
print('                                         -')
print(':Jogar no modo [SOLO] -> 1               -')
print(':Jogar no modo [VERSUS] -> 2             -')
print('                                         -')
print('------------------------------------------')

while (modo !=1 and modo!=2):

    modo = int(input('[Escolha o Modo]:'))
    if (modo<1 or modo>2):
        print("Entrada Inválida")

#CODIGO DO JOKEMPO

#MODO 1 JOGADOR
if (modo == 1):
    print()
    print('------Pontuação Player 1: |', pont_p1, '| -------')
    print('------Pontuação Pc      : |', pont_p2, '| -------')
    print()

    while (p1 != 0 and p2 != 0):

        p2 = random.randint(1,3)
        p1 = int(input('Player: [1]Pedra, [2]Papel, [3]Tesoura, [0]sair: '))
        print()

        #P1 PEDRA
        if (p1 == 1):

            if (p2 == 3):

                pont_p1 += 1
                print('PC: ', p2)
                print()
                print('------Pontuação Player : |', pont_p1,'| -------')
                print('------Pontuação PC     : |', pont_p2,'| -------')
                print()
                print("Pedra ganha de Tesoura")
                print('*Player 1 ganhou a rodada!')
                print()
                print('------------------------------------------')

            elif (p2 == 2):

                pont_p2 += 1
                print('PC: ', p2)
                print()                
                print('------Pontuação Player : |', pont_p1,'| -------')
                print('------Pontuação PC     : |', pont_p2,'| -------')
                print()
                print("Pedra perde para Papel")
                print('*PC ganhou a rodada!')
                print()
                print('------------------------------------------')

            elif (p2 == 1):
                print('PC: ', p2)
                print()
                print('------Pontuação Player : |', pont_p1,'| -------')
                print('------Pontuação PC     : |', pont_p2,'| -------')
                print()
                print("Ambos escolheram pedra")
                print('*A rodada empatou!')
                print()
                print('------------------------------------------')

        #P1 PAPEL
        elif (p1 == 2):

            if (p2 == 1):

                pont_p1 += 1
                print('PC: ', p2)
                print()
                print('------Pontuação Player : |', pont_p1,'| ----------')
                print('------Pontuação PC     : |', pont_p2,'| ----------')
                print()
                print("Papel ganha de Pedra")
                print('*Player ganhou a rodada!')
                print()
                print('------------------------------------------')

            elif (p2 == 3):

                pont_p2 += 1
                print('PC: ', p2)
                print()
                print('------Pontuação Player : |', pont_p1,'| ----------')
                print('------Pontuação PC     : |', pont_p2,'| ----------')
                print()
                print("Papel perde para Tesoura")
                print('*PC ganhou a rodada!')
                print()
                print('------------------------------------------')

            elif (p2 == 2):
                print('PC: ', p2)
                print()
                print('------Pontuação Player : |', pont_p1,'| -------')
                print('------Pontuação PC     : |', pont_p2,'| -------')
                print()
                print("Ambos escolheram Papel")
                print('*A rodada empatou!')
                print()
                print('------------------------------------------')

        #P1 TESOURA
        elif (p1 == 3):

            if (p2 == 2):

                pont_p1 += 1
                print('PC: ', p2)
                print()
                print('------Pontuação Player : |', pont_p1,'| ----------')
                print('------Pontuação PC     : |', pont_p2,'| ----------')
                print()
                print("Tesoura ganha de Papel ")
                print('*Player ganhou a rodada!')
                print()
                print('------------------------------------------')

            elif (p2 == 1):

                pont_p2 += 1
                print('PC: ', p2)
                print()
                print('------Pontuação Player : |', pont_p1,'| ----------')
                print('------Pontuação PC     :  |', pont_p2,'| ----------')
                print()
                print("Tesoura perde para Pedra")
                print('*PC ganhou a rodada!')
                print()
                print('------------------------------------------')
                
            elif (p2 == 3):
                print('PC: ', p2)
                print()
                print('------Pontuação Player : |', pont_p1,'| -------')
                print('------Pontuação PC     : |', pont_p2,'| -------')
                print()
                print("Ambos escolheram Tesoura")
                print('*A rodada empatou!')
                print()
                print('------------------------------------------')

        elif (p1 == 0):
            print("Saindo....")

        else:
            print("Número Inválido")
            print()

    print()
    print('-----------Pontuação Final-------------')
    print('------Pontuação Player 1: |', pont_p1, '| -------')
    print('------Pontuação Pc:       |', pont_p2, '| -------')
    print('---------------------------------------')

#MODO 2 JOGADORES
elif (modo == 2):
    print()
    print('------Pontuação Player 1: |', pont_p1, '| -------')
    print('------Pontuação Player 2: |', pont_p2, '| -------')
    print()

    while (p1 != 0 and p2 != 0):
        p2 = -1
        p1 = int(input('Player 1 - [1]Pedra, [2]Papel, [3]Tesoura, [0]sair: '))
        print()

        if (p1 == 0):
            print("Saindo........")
            break
        elif (p1 not in range1):
            print("Número inválido")
            print()
        else:
            while(p2 not in range1):
                p2 = int(input('Player 2 - [1]Pedra, [2]Papel, [3]Tesoura, [0]sair: '))
                print()
                if (p2 == 0):
                    print("Saindo........")
                    break
                if(p2 not in range1):
                    print("Número inválido")

            #P1 PEDRA
            if (p1 == 1):

                if (p2 == 3):

                    pont_p1 += 1
                    print('------Pontuação Player 1: |', pont_p1,'| -------')
                    print('------Pontuação Player 2: |', pont_p2,'| -------')
                    print()
                    print("Pedra ganha de Tesoura")
                    print('*Player 1 ganhou a rodada!')
                    print()
                    print('------------------------------------------')

                elif (p2 == 2):

                    pont_p2 += 1
                    print('------Pontuação Player 1: |', pont_p1,'| -------')
                    print('------Pontuação Player 2: |', pont_p2,'| -------')
                    print()
                    print("Pedra perde para Papel")
                    print('*Player 2 ganhou a rodada!')
                    print()
                    print('------------------------------------------')

                elif (p2 == 1):
                    print('------Pontuação Player 1: |', pont_p1,'| -------')
                    print('------Pontuação Player 2: |', pont_p2,'| -------')
                    print()
                    print("Ambos escolheram Pedra")
                    print('*A rodada empatou!')
                    print()
                    print('------------------------------------------')

            #P1 PAPEL
            elif (p1 == 2):

                if (p2 == 1):

                    pont_p1 += 1
                    print('------Pontuação Player 1: |', pont_p1,'| ----------')
                    print('------Pontuação Player 2: |', pont_p2,'| ----------')
                    print()
                    print("Papel ganha de Pedra")
                    print('*Player 1 ganhou a rodada!')
                    print()
                    print('------------------------------------------')

                elif (p2 == 3):

                    pont_p2 += 1
                    print('------Pontuação Player 1: |', pont_p1,'| ----------')
                    print('------Pontuação Player 2: |', pont_p2,'| ----------')
                    print()
                    print("Papel perde para Tesoura")
                    print('*Player 2 ganhou a rodada!')
                    print()
                    print('------------------------------------------')

                elif (p2 == 2):
                    print('------Pontuação Player 1: |', pont_p1,'| -------')
                    print('------Pontuação Player 2: |', pont_p2,'| -------')
                    print()
                    print("Ambos escolheram Papel")
                    print('*A rodada empatou!')
                    print()

                    print('------------------------------------------')
            #P1 TESOURA
            elif (p1 == 3):

                if (p2 == 2):

                    pont_p1 += 1
                    print('------Pontuação Player 1: |', pont_p1,'| ----------')
                    print('------Pontuação Player 2: |', pont_p2,'| ----------')
                    print()
                    print("Teosura ganha de Papel")
                    print('*Player 1 ganhou a rodada!')
                    print()
                    print('------------------------------------------')

                elif (p2 == 1):

                    pont_p2 += 1
                    print('------Pontuação Player 1: |', pont_p1,'| ----------')
                    print('------Pontuação Player 2: |', pont_p2,'| ----------')
                    print()
                    print("Tesoura perde para Pedra")
                    print('*Player 2 ganhou a rodada!')
                    print()
                    print('------------------------------------------')

                elif (p2 == 3):
                    print('------Pontuação Player 1: |', pont_p1,'| -------')
                    print('------Pontuação Player 2: |', pont_p2,'| -------')
                    print()
                    print("Ambos escolheram Tesoura")
                    print('*A rodada empatou!')
                    print()
                    print('------------------------------------------')

    print()
    print('-----------Pontuação Final-------------')
    print('------Pontuação Player 1: |', pont_p1,'| -------')
    print('------Pontuação Player 2: |', pont_p2,'| -------')
    print('---------------------------------------')

    



