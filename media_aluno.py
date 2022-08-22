#A partir de três notas de um aluno e informe o conceito a partir da média:

nota1 = float((input("Insira a nota 1:")))
nota2 = float((input("Insira a nota 2:")))
nota3 = float((input("Insira a nota 3:")))

media = ((nota1+nota2+nota3)/3)

if (0<media<=4.0):
    conceito = "E"
    rpv = "Sim"
elif (4.0<media<=6.0):
    conceito = "D"
    rpv = "Sim"
elif (6.0<media<=7.5):
    conceito = "C"
    rpv = "Não"
elif (7.5<media<=9.0):
    conceito = "B"
    rpv = "Não"
elif (9.0<media<=10):
    conceito = "A"
    rpv = "Não"

print("A média é %d, seu conceito é %s, Reprovado: %s" %(media,conceito,rpv))
