from random import randrange
from math import ceil
from time import sleep
import os, sys


def partie():
    """Fonction demandant au joueur de choisir un nombre entre 0 et 49"""
    pari = 'a'
    while pari.isnumeric() == False:
        pari = input("Choisissez un nombre entre 0 et 49 : ")
    return pari

def miser():
    """Fonction demandant au joueur de préciser sa mise"""
    mise = 'a'
    while mise.isnumeric() == False:
        mise = input("Combien voulez-vous miser ? ")
    return mise

def get_number():
    """Fonction utilisée pour tirer aléatoirement un nombre entre 0 et 49"""
    print("\nLes jeux sont faits rien ne va plus...")
    sleep(1)
    return randrange(50)

def result(pari, mise, number):
    """Fonction calculant le résultat du jeu"""
    print("Vous avez parier sur : {} et le résultat est : {}".format(pari, number))
    if pari == number:
        print("C'est gagné !")
        return mise
    elif (int(pari) % 2) == (int(number) % 2):
        print("Même couleur !")
        return ceil(mise * 0.5)
    else:
        print("C'est perdu !")
        return -mise

def jouer():
    """Fonction lançant la partie de ZCasino"""
    cagnotte = 1000
    print("Bienvenue au ZCasino !")

    play = True
    while play:

        if cagnotte <= 0:
            print("Vous êtes ruiné ! C'est la fin de la partie.")
            sys.exit(0)
        
        pari = partie()
        mise = int(miser())
        number = get_number()
        cagnotte += result(pari, mise, number)

        print("Vous avez : {} $".format(cagnotte))
        
        keep_going = 'z'
        while keep_going != 'y' or keep_going != 'n':
            keep_going = input("Voulez-vous continuer à jouer (y/n) ? ")
            keep_going = keep_going[0].lower()

            if keep_going == 'n':
                play = False
                print("A la revoyure !")
                sys.exit(0)
            if keep_going == 'y':
                break

if __name__=="__main__":
    jouer()
