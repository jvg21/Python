#VALIDADOR DE SENHA
Maiu = 0  #2
Num = 0   #2
Espec = 0 #3
n = 0
tam = 0
Senha = ""

while (tam<1 or tam>8):
    Senha = input("Digite a senha: ")
    tam = len(Senha)
    print(tam)

for i in range(0,tam):
    n = ord(Senha[i])
    print(n,Senha[i])

    if (65<=n<=90):
         Maiu += 1
         print("Maiuscula")

    elif (48<=n<=57):
        Num += 1
        print("Número")

    elif ((33<=n<=47) or (58<=n<=64) or 123<=n):
        Espec += 1
        print("Especial")

print(f"Maiusculas: {Maiu}, Números: {Num}, Especiais: {Espec}")

if (Maiu<2 or Num<2 or Espec<3):
    print("Senha Inválida")
else:
    print("Senha Valida")



