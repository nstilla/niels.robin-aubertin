"""
Pour cet été, il y aura 3 exercices croissants en difficulté.
Ils vont demander de parcourir la documentation python

Python vient par défaut avec certaines fonctions de base qu'on a utilisé jusqu'ici.
Vous pouvez les retrouver sur cette page : https://docs.python.org/fr/3/library/functions.html

Mais python arrive également avec plein de modules déjà tout faits.
Un module est un morceau de code fait par des développeurs que vous pouvez réutiliser dans le votre.

Un exemple est le module random : https://docs.python.org/fr/3/library/random.html
Ce module permet de générer des valeurs aléatoires.
Pour l'utiliser, on aurait du faire comme qui suit :
"""

# on commence par "importer" le module (on déclare qu'on va l'utiliser)
import random
# puis on appelle une fonction du module (ici randint)
# randint nous permet ici de simuler un jet de dé à 6 faces
entier_aléatoire = random.randint(1, 6)
print(f"Résultat du jet de dé à 6 faces : {entier_aleatoire}")

"""
Il y a plein de modules préfaits.
Voici la liste complète : https://docs.python.org/fr/3/py-modindex.html
Je vous pointerai du doigt quels modules utiliser dans chaque exo.
"""