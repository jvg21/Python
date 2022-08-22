# Adicione 50 números aleatórios (rand()) em um vetor. Calcule a média, desvio padrão, valores máximos e mínimos.
import random
vet = []
tamanho = []
med = 0
desvio = 0

# criar os valores randomicos do vetor
for i in range(0,50):
    vet.append(random.randint(0,200))

maior = vet[0]
menor = vet[0]

#Maior e menor
for i in range(0, 50):
    med += vet[i]
    if (vet[i]>maior):
        maior = vet[i]
    if (vet[i]<menor):
        menor = vet[i]

tamanho = len(vet)
med /= tamanho

for i in range(0,50):
    desvio += ((vet[i]-med)**2)

desvio = ((desvio/tamanho)**0.5)

print(f"Média: {med:.2f}")
print(f"Desvio: {desvio:.4f}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")


