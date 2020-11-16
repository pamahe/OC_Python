#!/bin/python3.8

class DicOrd:
    """Classe représentant un dictionnaire ordonné sous la forme de deux listes:
    clés et valeurs"""

    def __init__(self, dico=None, **couples):
        """Constructeur initialisant un dictionnaire ordonné de 3 manières différentes:
            - vide
            - à partir d'une dictionnaire Python classique
            - à partir de couples clé=valuer
        """
        self.cles = []
        self.valeurs = []
        if dico is not None:
            for cle, valeur in dico.items():
                self.cles.append(cle)
                self.valeurs.append(valeur)
        elif couples is not None:
            self.cles = list(couples.keys())
            self.valeurs = list(couples.values())

    def __setitem__(self, cle, valeur):
        """Assigne une nouvelle 'valeur' à l'index donné par 'cle'. Si 'cle' n'est pas présent, on rajoute le couple
        à la fin du dictionnaire"""
        try:
            index = self.cles.index(cle)
            self.valeurs[index] = valeur
        except ValueError:
            self.cles.append(cle)
            self.valeurs.append(valeur)

    def __getitem__(self, cle):
        """Retourne la valeur associée à la clé 'cle'"""
        index = self.cles.index(cle)
        return self.valeurs[index]

    def __delitem__(self, param):
        """Supprime le couple cle,valeur donné par le paramètre (cle ou index)"""
        try:
            index = param
            del self.cles[index]
            del self.valeurs[index]
        except TypeError:
            index = self.cles.index(param)
            del self.cles[index]
            del self.valeurs[index]

    def __len__(self):
        """Retourne la longueur du dictionnaire"""
        return len(self.cles)

    def __iter__(self):
        """Retourne un itérateur définit pour la classe DicOrd"""
        return ItDicOrd(self)

    def __add__(self, other):
        """Méthode permettant d'ajouter deux dictionnaires ordonnés"""
        nvlles_cles = self.cles + other.cles
        nvlles_valeurs = self.valeurs + other.valeurs
        dic = {}
        for i in range(len(nvlles_cles)):
            dic[nvlles_cles[i]] = nvlles_valeurs[i]
        return DicOrd(dic)

    def sort(self):
        """Méthode permettant de trier le dictionnaire en se basant sur l'ordre
        alphabétique des clés"""
        cles_ordo = sorted(self.cles)
        val_ordo = []
        for cle in cles_ordo:
            val_ordo.append(self[cle])
        self.cles = cles_ordo
        self.valeurs = val_ordo

    def reverse(self):
        """Méthode permettant de trier le dictionnaire en se basant sur l'ordre
        alphabétique inverse des clés"""
        cles_ordo = sorted(self.cles, reverse=True)
        val_ordo = []
        for cle in cles_ordo:
            val_ordo.append(self[cle])
        self.cles = cles_ordo
        self.valeurs = val_ordo

    def __repr__(self):
        """Méthode permettant l'affichage du dictionnaire dans l'interpréteur Python"""
        chaine = "{"
        for i in range(len(self.cles)):
            chaine += str(self.cles[i])
            chaine += ':'
            chaine += str(self.valeurs[i])
            if i < len(self.cles) - 1:
                chaine += ', '
        chaine += "}"
        return chaine


class ItDicOrd:
    """Un itérateur permettant de parcourir un DicOrd"""
    def __init__(self, dicord):
        self.cles = dicord.cles
        self.position = -1

    def __next__(self):
        """Cette méthode doit renvoyer l'élémént suivant dans le parcours
        ou lever l'exception 'StopIteration' si le parcours est fini"""
        if self.position == len(self.cles)-1:
            raise StopIteration
        self.position += 1
        return self.cles[self.position]
