#!/bin/python3.8

import time


def mon_decorateur(fonction):
    """Notre décorateur : il va afficher un message avant l'appel de la
    fonction définie"""

    def fonction_modifiee():
        """Fonction que l'on va renvoyer. Il s'agit en fait d'une version
        un peu modifiée de notre fonction originellement définie. On se
        contente d'afficher un avertissement avant d'exécuter notre fonction
        originellement définie"""

        print("Attention ! On appelle {0}".format(fonction))
        return fonction()
    return fonction_modifiee


# Un exemple qui paraît plus utile
def obsolete(fonction_origine):
    """Décorateur levant une exception pour noter que la fonction_origine
    est obsolete"""

    def fonction_modifiee():
        raise RuntimeError("La fonction {0} est obsolète !".format(fonction_origine))
    return fonction_modifiee()


@mon_decorateur
def salut():
    print("Salut !")


"""Pour gérer le temps, on importe le module time
On va utiliser surtout la fonction time() de ce module qui renvoie le nombre
de secondes écoulées depuis le premier janvier 1970 (habituellement).
On va s'en servir pour calculer le temps mis par notre fonction pour
s'exécuter"""


def controller_temps(nb_secs):
    """Contrôle le temps mis par une fonction pour s'exécuter.
    Si le temps d'exécution est supérieur à nb_secs, on affiche une alerte"""

    def decorateur(fonction_a_executer):
        """Notre décorateur. C'est lui qui est appellé directement LORS
        DE LA DEFINITION de notre fonction (fonction_a_executer)"""

        def fonction_modifiee(*parametres_non_nommes, **parametres_nommes):
            """Fonction renvoyée par notre décorateur. Elle se charge
            de calculer le temps mis par la fonction à s'exécuter"""

            tps_avant = time.time()
            valeur_renvoyee = fonction_a_executer(*parametres_non_nommes, **parametres_nommes)
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant
            if tps_execution >= nb_secs:
                print("La fonction {0} a mis {1} pour s'exécuter".format(
                    fonction_a_executer, tps_execution))
            return valeur_renvoyee
        return fonction_modifiee
    return decorateur


def singleton(classe_definie):
    instances = {}  # Dictionnaire de nos instances singletons

    def get_instance():
        if classe_definie not in instances:
            # On crée notre premier objet de classe_definie
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]
    return get_instance


def controller_types(*a_args, **a_kwargs):
    """On attend en paramètres du décorateur les types souhaités. On accepte
    une liste de paramètres indéterminés, étant donné que notre fonction
    définie pourra être appelée avec un nombre variable de paramètres et que
    chacun doit être contrôlé"""

    def decorateur(fonction_a_executer):
        """Notre décorateur. Il doit renvoyer la fonction_modifiee"""
        def fonction_modifiee(*args, **kwargs):
            """Notre fonction modifiee. Elle se charge de contrôler
            les types qu'on lui passe en paramètres"""

            # La liste des paramètres attendus (a_args) doit être de même
            # Longueur que celle reçue (args)
            if len(a_args) != len(args):
                raise TypeError("le nombre d'arguments attendu n'est pas égal au nombre reçu")
            # On parcourt la liste des arguments reçus et non nommés
            for i, arg in enumerate(args):
                if a_args[i] is not type(args[i]):
                    raise TypeError("l'argument {0} n'est pas du type {1}".format(
                        i, a_args[i]
                    ))

            # On parcourt maintenant la liste des paramètres reçus et nommés
            for cle in kwargs:
                if cle not in a_kwargs:
                    raise TypeError("l'argument {0} n'a aucun type précisé".format(
                        repr(cle)
                    ))
                if a_kwargs[cle] is not type(kwargs[cle]):
                    raise TypeError("l'argument {0} n'est pas de type {1}".format(
                        repr(cle), a_kwargs[cle]
                    ))
            return fonction_a_executer(*args, **kwargs)
        return fonction_modifiee
    return decorateur


@controller_types(int, int)
def intervalle(borne_inf, borne_sup):
    print("Intervalle de {0} à {1}".format(borne_inf, borne_sup))


if __name__ == "__main__":
    salut()
    print(salut)
    intervalle(1, 8)
    intervalle(5, "oups")
