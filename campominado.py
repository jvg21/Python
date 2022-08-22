import random

cmp = []
for l in range(0,10):
    cmp.append([])
    for c in range(0,10):
        cmp[l].append(random.randint(0,1))

bmb = 0
while(bmb==0):
    linha = int(input("Digite a linha(1 até 10): "))
    coluna = int(input("Digite a coluna(1 até 10): "))
    linha -= 1
    coluna -= 1
    if (linha<0 or linha>9 or coluna<0 or coluna>9):
        print("Célula inválida")
        break
    elif(cmp[linha][coluna]==1):
        print("BOOOOOOOM")
        break
    else:
        print("Célula vazia")




