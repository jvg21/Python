import random

def Fmax(vet):#Maior elemento de um vetor
    max = vet[0]
    tam = len(vet)
    for i in range(0,tam):
        if max<vet[i]:
            max = vet[i]

    return max

def Fmin(vet):#Menor Elemento de um vetor
    min = vet[0]
    tam = len(vet)
    for i in range(0,tam):
        if vet[i]<min:
            min = vet[i]

    return min

def Finverte(vet):#Inverte um vetor númerico
    tam = len(vet)-1
    vet2 = []
    for i in range(tam,-1,-1):
        vet2.append(vet[i])

    return vet2

def Flower(text): #Converte todas as letras para minusculas
    text = str(text)
    text2 = ""
    tam = len(text)

    for i in range(0,tam):
        n = ord(text[i])
        if (65<=n<=90):
            text2 += chr(n+32)
        else:
            text2 += text[i]
    return text2

def Fupper(text): #Converte todas as letras para maiusculas
    text = str(text)
    text2 = ""
    tam = len(text)

    for i in range(0,tam):
        n = ord(text[i])
        if (97<=n<=122):
            text2 += chr(n-32)
        else:
            text2 += text[i]

    return text2

vet = []
texto = 'Teste Exercico RA'
for i in range(0,10):
    vet.append(random.randint(0,100))

print(vet,"\nMaior elemento: ",Fmax(vet))
print()
print(vet,"\nMenor elemento: ",Fmin(vet))
print()
print(vet,"Invertida: ",Finverte(vet))
print()
print(texto,',',Flower(texto))
print(texto,',',Fupper(texto))


