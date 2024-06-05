def Forca(tentativa):
    f1 = " +-------+   "
    f2 = " |           "
    f3 = " |           "
    f4 = " |           "
    f5 = " |           "
    f6 = " |           "
    f7 = "_|_          "

    if tentativa >= 1:
        f2 = " |       | "
    if tentativa >= 2:
        f3 = " |       O "
    if tentativa >= 3:
        f4 = " |      /|\ "
    if tentativa >= 4:
        f5 = " |       | "
    if tentativa >= 5:
        f6 = " |      / \ "



    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
    print(f6)
    print(f7)

def Continue():
    while True:
        print("" * 20)
        novamete = input("Quer jogar de novo S/N: ").upper()
        if novamete == "S":
            Acabou = True
            break
        elif novamete == "N":
            Acabou = False
            break
        else:
            print("Digite S ou N")
    return Acabou

def sorteiapalavra():
    lista = ["amor","boiceta ","totatola","menort","discoteca","grama","casamento","japones","tonycontry"]
    return random.choice(lista)

def apresentapalavra (letras, palavras):
    npalavra= " _ " * len(palavras)
    for L in range (0 ,len(letras)):
        print(letras[L])   

    return npalavra  

import random


##Jogar = True
#x=0
##while Jogar :
 ##   Forca(x)
  ##  Jogar = Continue()
   ##ss x = x + 1
Forca (10)

print(sorteiapalavra())

print (apresentapalavra("ABX","abacaxi"))



       
