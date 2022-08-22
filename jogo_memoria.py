#Jogo da memória
import random
import sys
import time

# funções:

def matrizmemoria(n):  # cria as matrizes com n*n espaços
    mat = []
    mat2 = []
    # popula as duas matrizes com #
    for l in range(0, n):
        mat.append([])
        mat2.append([])
        for c in range(0, n):
            mat[l].append("@")
            mat2[l].append("-")

    # altera a segunda matriz para letras
    for l in range(0, n):
        for c in range(0, int(n / 2)):
            chara = chr(random.randint(65, 90))
            mat2[l][c] = chara
            mat2[l][c + int(n / 2)] = chara

    return (mat, mat2)

def embaralhar(mat):
    taml = len(mat)  # quantidade de linhas
    tamc = len(mat[0])  # quantidade de colunas

    for vzs in range(0, 5):  # vezes embaralhadas
        # embaralhar linhas
        for linha in range(0, taml):
            # pega o indice de uma coluna dentro da linha e inverte com outro indice aleatório(ram)
            for coluna in range(0, tamc):
                # tratamento para não pegar o mesmo indice
                ram = coluna
                while ram == coluna:
                    ram = random.randint(0, tamc - 1)  # pega um indice de coluna aleatório

                mat[linha][coluna], mat[linha][ram] = mat[linha][ram], mat[linha][coluna]  # inverte os valores

        # embaralhar colunas
        for coluna in range(0, tamc):
            for linha in range(0, taml):
                ram = linha
                while ram == linha:
                    ram = random.randint(0, taml - 1)

                mat[linha][coluna], mat[ram][coluna] = mat[ram][coluna], mat[linha][coluna]

    return mat


# printa matrizes
def Pmat(mat):
    tam = len(mat)
    for i in range(0, tam):
        print(f"Linha:{i + 1} {mat[i]}")

def GetI(oculto):
    posicao = []
    tam = len(oculto)

    for jogada in range(1, 3):
        aux = 0
        while aux == 0:
            l = int(input(f"Digite a linha para a jogada {jogada}: "))
            # verifica se o indice existe
            if (-1 < (l - 1) < tam):
                posicao.append((l - 1))  # corrige para o indice da matriz ja que o input é feito por elemento
                aux = 1
            else:
                print("Linha inválida")

        aux = 0
        while aux == 0:
            c = int(input(f"Digite a coluna para a jogada {jogada}: "))

            if (-1 < (c - 1) < tam):
                posicao.append((c - 1))
                aux = 1
            else:
                print("Coluna inválida")

        print(f"Jogada {jogada} [{l}],[{c}]")
        print()
    return posicao  # retorna um vetor com os indices jogados


print("#---------------------------------JOGO DA MEMÓRIA--------------------------------------------#")
n = int(input("Digite a dificuldade: [1]Fácil, [2]Médio, [3]Difícil: "))

if n == 1:
    n = 4
elif n == 2:
    n = 8
elif n == 3:
    n = 10
else:
    print("Entrada inválida")
    sys.exit()

print('\n' *100)
jogo = True
ajudas = 2
pontomax = n * n
pontoatual = 0

oculto, visivel = matrizmemoria(n)
visivel = embaralhar(visivel)

while jogo == True:

    aux = 0
    while aux == 0:
        print("#---------------------------------JOGO DA MEMÓRIA--------------------------------------------#")
        print(f"Pontuação: {pontoatual}, Ajudas: {ajudas}")
        #Pmat(visivel)
        print()
        Pmat(oculto)
        print()

        x = int(input("Jogar[1], Ajuda[2], sair[0]: "))
        if x == 1:
            aux = 1
        elif x == 2 and ajudas > 0:
            ajudas -= 1
            print('\n' *100)
            Pmat(visivel)
            time.sleep(4)
            print('\n' *100)
        elif x == 2 and ajudas <= 0:
            print("Sem Ajudas Disponiveis")
            time.sleep(1)
            print('\n' *100)
        elif x == 0:
            print("Saindo.......")
            sys.exit()
        else:
            print('\n' *100)
            print("Entrada Inválida!")

    print()
    P = GetI(oculto)  # P guarda as posições jogadas(indices)
    # print(P)
    if (P[0] == P[2] and P[1] == P[3]):  # verifica se as duas jogadas não estão na mesma casa
        print("Jogada Inválida. Por favor selecione casas diferentes")

    elif ((oculto[P[0]][P[1]]) != '@' or (oculto[P[2]][P[3]]) != '@'):  # verifica se a casa já não foi descoberta
        print("Jogada Inválida. Por favor selecione casa ainda não descobertas")
    else:
        print(f"Jogada 1: {visivel[P[0]][P[1]]}, Jogada2: {visivel[P[2]][P[3]]}")
        if visivel[P[0]][P[1]] == visivel[P[2]][P[3]]:
            oculto[P[0]][P[1]] = visivel[P[0]][P[1]]
            oculto[P[2]][P[3]] = visivel[P[2]][P[3]]
            pontoatual += 2
            print("Parabéns jogada correta")
            print(f"Pontuação: {pontoatual}")
            Pmat(oculto)
        else:
            print("Jogada errada, tente novamente")
            Pmat(oculto)
    time.sleep(4)
    print('\n' *100)
    if pontoatual == pontomax:
        print("Parabens você venceu")
        jogo = False

