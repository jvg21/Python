#Jogo simples de acertar operações matemáticas
# Grupo:
# João Vitor Gregorini
# João Victor Ribeiro Basso
# Bruno Renan Guttervill
# Giovanni Lucca Uchôa
# Guilherme Lopes Cruz
import random
#Var
tentativas = 0
erros = 0
acertos = 0
soma = False
sub = False
mult = False
div = False

while (acertos<4):
    tentativas += 1

    #soma
    if (soma != True):
        x = random.randint(0,2000)
        y = random.randint(1,2000)
        soma = int(input(f"Qual é o resultado da soma: {x} + {y} ?"))
        if(soma == (x + y)):
            acertos+=1
            soma = True
            print("Soma correta")
        else:
            print("Soma incorreta")
            erros += 1
            soma = False
        print()

    #Subtração
    if (sub != True):
        x = random.randint(1,2000)
        y = random.randint(1,2000)
        sub = int(input(f"Qual é o resultado da subtração: {x} - {y} ?"))

        if(sub == (x - y)):
            acertos += 1
            sub = True
            print("Subtração correta")
        else:
            print("Subtração incorreta")
            sub = False
            erros += 1
        print()

    #Multiplicação
    if (mult != True):
        x = random.randint(-200,200)
        y = random.randint(-20,100)
        mult = int(input(f"Qual é o resultado da multiplicação: {x} x {y} ?"))

        if(mult == (x * y)):
            acertos += 1
            mult = True
            print("Multiplicação correta")
        else:
            print("Multiplicação incorreta")
            erros += 1
            mult = False
        print()

    #Divisão
    if (div != True):
        x = random.randint(10,1000)
        y = random.randint(1,50)
        div = int(input(f"Qual é o resultado inteiro da divisão: {x} / {y} ?"))

        if(div == (x // y)):
            acertos += 1
            div = True
            print("Divisão correta")
        else:
            print("Divisão incorreta")
            erros += 1
            div = False
        print()

    input("Pressione uma tecla para continuar......")
    print()

print("Parabéns você concluiu o desafio")
print(f"Você teve {erros} erros em {tentativas} tentativas")



        
   



