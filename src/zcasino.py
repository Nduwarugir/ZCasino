# -*-coding:utf-8 -*

from random import randrange
from math import ceil


def zcasino(argent):
    print("Bienvenu au ZCasino... \nVous commencez avec", argent, "$")

    continuer = True
    i = 1
    while continuer:
        print("\n***\n*** Tour", i, "\n***\n")
        win = randrange(50)
        choice = -1

        while choice < 0 or choice > 49:
            choice = input("Votre choix: ")
            try:
                choice = int(choice)
            except ValueError:
                print("Vous devez entrer un entier...")
                choice = -1
                continue
            if choice < 0:
                print("Votre choix ne peut etre négatif")
            if choice > 49:
                print("Votre choix ne peut excéder 49")

        mise = 0
        while mise <= 0 or mise > argent:
            mise = input("Votre Mise: ")
            try:
                mise = int(mise)
            except ValueError:
                print("Vous devez entrer un entier...")
                mise = -1
                continue
            if mise <= 0:
                print("Votre mise ne peut etre négatif")
            if mise > argent:
                print("Votre mise ne peut excéder votre somme")

        if mise == win:
            argent += 3 * mise
            print("Félicitations... Vous avez trouvé le numéro gagnant !!! Votre gain est de", 3 * mise, "$")
        elif mise % 2 == win % 2:
            argent += ceil(0.5 * mise)
            print("Félicitations... Vous avez trouvé la couleur gagnante !!! Votre gain est de", ceil(0.5 * mise), "$")
        else:
            argent -= mise
            print("Dommage... Une prochaine fois. Vous perdez", mise, "$")

        if argent <= 0:
            print("\n***\n*** Désolé mais vous etes à sec... À la prochaine !\n***\n")
            continuer = False
        else:
            print("Votre somme est:", argent, "$")
            reload = input("Continuer (o/n): ")
            if reload.lower() == 'o':
                continuer = True
                i += 1
            else:
                continuer = False


if __name__ == '__main__':
    somme = -1

    while somme < 0:
        somme = input("Entrer votre somme d'argent: ")
        try:
            somme = int(somme)
        except ValueError:
            somme = -1
            print("Vous devez entrer une valeur entière...")
            continue

    zcasino(argent=somme)
