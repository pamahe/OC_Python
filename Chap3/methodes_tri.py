#!/bin/python3.8

class Etudiant:

    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prénom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Etudiant {} (âge={}, moyenne={}>".format(
            self.prenom, self.age, self.moyenne)
