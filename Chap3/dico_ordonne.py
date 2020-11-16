#!/bin/python3.8

class DicOrd:

    """Classe représentant un dictionnaire ordonné sous la forme
    de deux listes : clés et valeurs."""

    def __init__(self, dico=None, **couples):
        """Constructeur initialisant un dico_ordonne vide"""
        self.keys = []
        self.values = []
        if dico != None:
            for cle, valeur in dico.items():
                self.keys.append(cle)
                self.values.append(valeur)
        elif couples != None:
            self.keys = list(couples.keys())
            self.values = list(couples.values())
    

    def __delitem__(self, param):
        """Delete the key, value couple with 'index' or 'key'"""
        try:
            index = param
            del self.keys[index]
            del self.values[index]
        except TypeError:
            index = self.keys.index(param)
            del self.keys[index]
            del self.values[index]

    def __getitem__(self,key):
        """Get the value associated with the given 'key'"""
        index = self.keys.index(key)
        return self.values[index]

    def __setitem__(self,key, value):
        """Assign a new value at the index given by 'key'"""
        try:
            index = self.keys.index(key)
            self.values[index] = value
        except ValueError:
            self.keys.append(key)
            self.values.append(value)

    def __len__(self):
        """Return the length of the dictionnary"""
        return len(self.keys)

    def __iter__(self):
        return ItDicOrd(self)



class ItDicOrd:
    """Un itérataur permettant de parcourir un DicOrd"""
    def __init__(self, dicord):
        self.dicord = dicord.keys
        self.position = -1

    def __next__(self):
        """Cette méthode doit renvoyer l'élémént suivant dans le parcours
        ou lever l'exception 'StopIteration' si le parcours est fini"""
        if self.position == len(self.dicord)-1:
            raise StopIteration
        self.position += 1
        return self.dicord[self.position]
