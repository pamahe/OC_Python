#!/bin/python3.8

"""Ce fichier définit toutes les fonctions qui sont utilisées par le
programme pendu"""

import pickle
import os
import random

from donnees import nb_coups, nom_fichier_scores, liste_mots


def welcome():
    """Fonction affichant l'écran de bienvenue et demandant le 
    pseudo du joueur"""
    print("   ***** Bienvenue au jeu du pendu ! *****")
    pseudo = input("\nComment vous appellez-vous ?\n")
    return pseudo

def load_score(pseudo):
    """Fonction qui charge le score du joueur. Si le fichier scores n'existe pas
    il est crée. Si le joueurs n'existe pas, on lui attribue un score de 0."""
    if os.path.exists(nom_fichier_scores):
        with(open(nom_fichier_scores, 'rb')) as file:
             loader = pickle.Unpickler(file)
             scores = loader.load()
             try:
                 player_score = scores[pseudo]
                 print(f"Bon retour {pseudo} !", end=' ')
                 print(f"Votre score est de {scores[pseudo]} !")
                 return scores
             except KeyError:
                 print(f"Un nouveau joueur ! Enchanté {pseudo} !", end=' ')
                 print("Votre score est actuellement de 0 points.")
                 print("Pas d'inquiétudes, il augmentera très vite !")
                 scores[pseudo] = 0
                 return scores
    else:
        open(nom_fichier_scores, 'w').close()
        print(f"Vous êtes notre premier joueur {pseudo} !",end=' ')
        print("Votre score est actuellement de 0 points.")
        print("Pas d'inquiétudes ! Il augmentera très vite !")
        scores = {pseudo: 0}
        return scores

def save_score(scores):
    """Fonction sauvegardant les scores après chaque fin de partie"""
    with open(nom_fichier_scores, 'wb') as file:
        saver = pickle.Pickler(file)
        saver.dump(scores)
    return None
        
def clear_screen():
    """Fonction utilisée pour changer d'écran. Nettoie tout affichage après
    que le joueur ait appuyé sur Entrée."""
    key = input("Appuyez sur Entrée pour continuer.")
    _ = os.system('clear')
    return None
    
def rules():
    """Fonction qui affiche les règles à l'écran"""
    print("Voici le déroulement de la partie : ")
    print("L'ordinateur choisi un mot au hasard, huit lettres maximums.")
    print("Le joueur tente de trouver les lettres composant le mot.")
    print("Le joueur à huit chances.")
    print("\n")
    print("A la fin de la partie, le nombre de coups restants est ajouté au score du joueur.\n")
    return None

def choose_word():
    """Fonction qui choisit aléatoirement un mot dans la liste données"""
    return random.choice(liste_mots)

def screen(mot, lettres_choisies, coups_restants):
    """Fonction qui affiche l'écran de déroulementde la partie"""
    vraies_lettres = [elt for elt in mot]
    hidden_word = ['*' for elt in mot]
    print("\t\t Mot caché : ", ''.join(hidden_word))
    print("Lettres essayées : ", ' '.join(lettres_choisies))
    lettre = '-1'
    while lettre.isalpha() == False and lettre not in lettres_choisies:
        lettre = str(input("\nChoisissez une lettre : ")).upper()
        
    lettres_choisies.append(lettre)
    trouve = 0
    for i in range(len(mot)):
        if lettre == mot[i]:
            hidden_word[i] == lettre
            trouve += 1
            print(f"Lettre {lettre} trouvé dans le mot caché !")
    if trouve == 0:
        coups_restants -=1
        print(f"La lettre {lettre} n'est pas présente dans le mot caché ! ")

    if '*' in hidden_word:
        resultat = 0
    if coups_restants == 0:
        resultat = -1
    elif:
        
        resultat = 1
    print('resultat = ', resultat)
    return mot, lettres_choisies, coups_restants, resultat
