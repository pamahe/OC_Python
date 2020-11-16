#!/usr/bin/python3.8

# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

annee = input("Saisissez une année : ") # On attend que l'utilisateur fournisse l'année qu'il désire tester

try: # On essaye de convertir l'année en entier
    annee = int(annee) # Risque d'erreur si l'utilisateur ne saisit pas un nombre
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")
    
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")
