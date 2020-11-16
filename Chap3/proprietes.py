#!/bin/python3.8

class Personne:
    """Classe définissant une personne caractérisée par:
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""


    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = 'Paris' # Notez l'underscore _ devant le nom

    def _get_lieu_residence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut 'lieu_residence'"""
        print("On accède à l'attribut lieu_residence :")
        return self._lieu_residence

    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}".format(self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence

    # On va dire à Python que notre attribut lieu_residence pointe vers une propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Personne : nom({}), prénom({}), âge({})".format(self.nom, self.prenom, self.age)
    
    def __str__(self):
        """Methode permettant d'afficher plus joliment notre objet"""
        return "{} {}, âgé de {} ans.".format(self.nom, self.prenom, self.age)

    
class Protege:
    """Classe possédant une méthode particulière d'accès à ses attributs :
    Si l'attribut n'est pas trouvé, on affiche une alerte et on renvoie None"""


    def __init__(self):
        """On crée quelques attributs par défaut"""
        self.a = 1
        self.b = 2
        self.C = 3

    def __getattr__(self,nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
        cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))

    def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée quand on fait objet.nom_attr = val_attr .
        On se charge d'enregistrer l'objet"""

        object.__setattr__(self, nom_attrn, val_attr)
        self.enregistrer()

        def __delattr__(self, nom_attr):
            """On ne peut supprimer d'attribut, on lève l'exception
            AttributeError"""
            raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")

##### Les méthodes de conteneur

class ZDict:
    """Classe enveloppe d'un dictionnaire"""
    def __init__(self):
        """Notre classe n'accepte aucun paramètre"""
        self._dictionnaire = {}
        
    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        return self._dictionnaire[index]

    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        self._dictionnaire[index] = valeur

    def __contains__(self, valeur):
        """Cette méthode est appelée quand on écrit valeur in objet"""
        return valeur in self._dictionnaire.values()

    def __len__(self):
        """Cette méthode est appelée quand on écrite len(objet)"""
        return len(self._dictionnaire)


##### Les méthodes mathématiques

class Duree:
    """Classe contenant des durées sous la forme d'un nombre de minutes
    et de secondes"""

    def __init__(self, min=0, sec=0):
        """Constructeur de la classe"""
        self.min = min
        self.sec = sec
    def __str__(self):
        """Affichage un peu plus joli de nos objets"""
        return "{0:02}:{1:02}".format(self.min, self.sec)

    def __add__(self, objet_a_ajouter):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        nouvelle_duree = Duree()
        # On va copier self dans l'objet créé pour avoir la même durée
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec
        # On ajoute la durée
        nouvelle_duree.sec += objet_a_ajouter
        # Si le nombre de secondes >= 60
        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60
        # On renvoie la nouvelle durée
        return nouvelle_duree

    def __radd__(self, objet_a_ajouter):
        """Cette méthode est appelée si on écrit 4 + objet et que 
        le premier objet (4 dans cet exemple) ne sait pas comment ajouter
        le second. On se contente de rediriger sur __add__ puisque, 
        ici, cela revient au même : l'opération doit avoir le même résiultat,
        posée dans un sens ou dans l'autre"""
        return self + objet_a_ajouter

    def __iadd__(self, objet_a_ajouter):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        # On travaille directement sur self cette fois
        # On ajoute la durée
        self.sec += objet_a_ajouter
        # Si le nombre de secondes >= 60
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec = self.sec % 60
        # On renvoie self
        return self

    def __eq__(self, autre_duree):
        """Test si self et autre_duree sont égales"""
        return self.sec == autre_duree.sec and self.min == autre_duree.min
    def __gt__(self, autre_duree):
        """Test si self > autre_duree"""
        # On calcule le nombre de secondes de self et autre_duree
        nb_sec1 = self.sec + self.min * 60
        nb_sec2 = autre_duree.sec + autre_duree.min * 60
        return nb_sec1 > nb_sec2

# Des méthodes spéciales utiles à Pickle

class Temp:
    """Classe contenant plusieurs attributs, dont un temporaire"""

    def __init__(self):
        """Constructeur de notre objet"""
        self.attr_1 = "une valeur"
        self.attr_2 = "une autre valeur"
        self.attr_temp = 5

    def __getstate__(self):
        """Renvoie le dictionnaire d'attributs à sérialiser"""
        dict_attr = dict(self.__dict__)
        dict_attr["attr_temp"] = 0
        return dict_attr

    def __setstate__(self, dict_attr):
        """Méthode appelée lors de la désérialisation de l'objet"""
        dict_attr["attribut_temporaire"] = 0
        self.__dict__ = dict_attr
