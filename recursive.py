# exemple d'une fonction récursive
# une fonction récursive s'appelle elle-même
# elle fait une espèce de boucle. Pas loin de la boucle while dans l'idée

# ici on fait une fonction qui va sommer les valeurs d'une liste
# elle va parcourir les éléments de la liste au fur et à mesure de ses appels
# elle va finir avec l'indice 0 et faire toutes les sommes à la fin
def somme(liste, indice):
    if indice == 0:
        return liste[0]
    return liste[indice] + somme(liste, indice - 1)

a = [1, 2, 3, 4]
resultat = somme(a, len(a) - 1)
print(resultat)