#!/bin/python3.8

class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""
    
    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self.lieu_residence = "Paris"


class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    objet_crees = 0
    def __init__(self):
        """A chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objet_crees += 1

    def combien(cls):
        """Méthode de classe affichant combien d'objets ont été crées"""
        print(f"Jusqu'à présent, {cls.objet_crees} ont été crées.")
    combien = classmethod(combien)

class Test:
    """Une classe de test tout simplement"""
    def afficher():
        """Fonction chargée d'afficher quelque chose"""
        print("On affiche la même chose")
        print("peu import les données de l'objet ou de la classe.")
    afficher = staticmethod(afficher)

        
class TableauNoir:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer par jeu de méthodes. L'attribut modifié
    est 'surface'"""


    def __init__(self):
        """Par défaut notre surface est vide"""
        self.surface = ""
        
    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""


        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):
        """Cette méthode se charge d'afficher, grâce à print,
        la surface du tableau"""
        print(self.surface)

    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface = ""
