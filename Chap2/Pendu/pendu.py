#!/bin/python3.8

"""Programme du pendu, les fonctions sont définis dans le fichier fonction.py
et les variables utiles dans le fichier donnees.py"""

from fonctions import *
from donnees import nb_coups

# Acceuil du joueur
pseudo = welcome()
scores = load_score(pseudo)
clear_screen()

# Présentation des règles
rules()
clear_screen()

# Boucle de partie
mot = choose_word()
coups_restants = nb_coups
lettres_choisies = []

resultat = 0

while resultat == 0:
    mot, lettres_choisies, coups_restants, resultat = screen(mot, lettres_choisies, coups_restants)
    clear_screen()
    
# Enregistrement des scores et sortie
save_score(scores)
