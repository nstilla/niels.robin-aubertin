# voici un exemple de fonction qui prend deux arguments
def add(a, b):
    # schtroumpf n'a pas d'existence en dehors de la fonction
    # on dit que c'est une variable locale
    schtroumpf = a + a + a
    # return renvoie la valeur de l'expression à sa droite
    # c'est la dernière opération d'une fonction
    return a + b

# une fonction peut en appeler une autre
def add_1(a):
    return add(a, 1)

# on peut manipuler une valeur de retour comme tout autre valeur
c = add_1(5)
print(c)

# une condition toujours vraie
if True:
    print("ceci est toujours executé")

# une condition toujours fausse
if False:
    print("ceci ne sera jamais executé")

# une condition toujours vraie
# à condition que la fonction add_1 ajoute bien 1
if add_1(4) > 3:
    print("5 est effectivement supérieur à 3")
else:
    print("je ne comprends plus les maths")

# une condition doit être une expression qui sera évaluée à vrai ou faux
# une comparaison (==, <, >, <=, >=, !=) sont des opérateurs
# qui comparent la partie à gauche et la partie
# à droite pour renvoyer une valeur de vérité (boolean)
c = 0
if add(c, 2) == 4:
    print("c vaut 2")
elif c == 0:
    print("c vaut 0")
else:
    print("c vaut autre chose")

## types vus jusqu'ici
# str: "chaine"
# int: 4
# bool: True, False

# exemples de conversions de valeurs vers un boolean
bool(0) # False
bool(1) # True
bool(1 == 1) # True
bool("") # False
bool(" ") # True
bool("coucou") # True

# faire qqch tant que "condition"
# la boucle while teste sa condition avant d'executer le bloc d'instructions
# a la fin des instructions, on recommence
# dès que la condition est fausse, on continue après le bloc
c = 0
while c < 10:
    c = c + 1
    print(c)

# on peut faire des listes de valeurs
ma_liste = ["a", "b", "c"]
# pour accéder à une valeur de la liste, il faut préciser l'indice de la valeur dans la liste
# attention : le premier indice est 0 pas 1
ma_liste[0] == "a" # True

# On peut ajouter une valeur à une liste avec append :
ma_liste.append("d")
ma_liste[4] == "d" # True

# la boucle for va attribuer tour à tour toutes les valeurs qu'il rencontre
# à la variable locale dont on a décidé le nom et executer les instructions de son bloc
# ici, i vaut tour à tour 0, puis 1, puis 2...
# range(n) = [0, 1, 2, ..., n-1]
for i in range(10):
    print(i)