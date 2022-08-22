#Detetive: Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.

p1 = input("Telefonou para a vítima?")
p2 = input("Esteve no local do crime?")
p3 = input("Mora perto da vítima?")
p4 = input("Devia para a vítima?")
p5 = input("Já trabalhou com a vítima?")
con = 0
if (p1 == "sim"):
     con = con+1
if (p2 == "sim"):
     con = con+1
if (p3 == "sim"):
     con = con+1
if (p4 == "sim"):
     con = con+1
if (p5 == "sim"):
     con = con+1

if (con == 5):
    print("Assassino")
elif (con==4 or con==3):
    print("Cúmplice")
elif (con==1 or con==2):
    print("Suspeito")
else:
    print("Inocente")

