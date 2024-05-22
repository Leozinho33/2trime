def Forca(Tentativa):
    f1 = "      |-+-----+-|     "
    f2 = "      |         |     "
    f3 = "      |         0     "
    f4 = "      |        /|\    "
    f5 = "      |         |     "
    f6 = "      |        / \    "
    f7 = "______|______________ "
   id tentativa>= 1:
        f2




def Continua ():
    while True:
        print("-" * 20)
        novamente = input("Quer jogar de novo S/N: ").upper()
        if novamente == "S":
            Acabou = True
            break
        elif novamente == "N":
            Acabou = False
            break
    else:
        print("digite S ou N")
        return Acabou
jogar = True
while jogar :
    jogar = Continua()
