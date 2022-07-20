# Exemple de programme pour le chiffre de César
# Ici je décide de n'utiliser que ce qu'on a appris lors des derniers cours
# Je vais convertir les majuscules en minuscules et décaler (chifrer) les lettres uniquement
# exemple de résultat
# "Coucou les gars !" (+1) => "dpvdpv mft hbst !"
# C => c => 3 => 4 => d

# fonction qui vérifie si une lettre doit être chiffrée ou non
# on ne chiffre que ce qui est une lettre minuscule non accentuée
def doit_etre_chiffre(lettre):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # on parcoure notre alphabet pour voir si on trouve la lettre demandée
    for l in alphabet:
        # si on trouve la lettre demandée, on renvoie vrai
        if lettre == l:
            return True
    # si on a parcouru tout notre alphabet sans trouver la lettre
    # alors c'est qu'elle n'est pas dedans. On renvoie faux.
    return False

# Cette fonction transforme les majuscules en minuscules
def majuscule_vers_minuscule(lettre):
    alphabet_majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_minuscules = "abcdefghijklmnopqrstuvwxyz"
    # on maintient un nombre en mémoire correspondant au numéro de la lettre
    nombre = -1
    for l in alphabet_majuscules:
        # a chaque fois qu'on avance dans l'alphabet
        # il faut mettre à jour nombre en l'incrémentant
        nombre = nombre + 1
        if lettre == l:
            # si on trouve notre lettre majuscule
            # alors on renvoie la minuscule correspondante
            return alphabet_minuscules[nombre]
    # si on a pas trouvé notre lettre
    # alors ce n'est pas une majuscule à convertir
    return lettre

# fonction qui prend une lettre en entrée et qui sort un nombre
def lettre_vers_nombre(lettre):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # nombre représente le nombre de la lettre en cours de comparaison
    nombre = 1
    for l in alphabet:
        if lettre == l:
            # si c'est notre lettre, on la renvoie
            return nombre
        else:
            # sinon, il faut ajouter 1 à nombre avant de passer
            # à la lettre suivante
            nombre = nombre + 1
    # le code ne devrait pas arriver ici
    # parce qu'on va appeler cette fonction que pour des lettres
    # qui sont dans l'alphabet

# fonction qui prend un nombre en entrée et qui sort une lettre
def nombre_vers_lettre(nombre):
    # pour pouvoir gérer un nombre négatif
    # (qui peut apparaitre lors d'un décalage négatif)
    # on va ajouter 26 au nombre
    nombre = nombre + 26
    # Ici, on est astucieux et on étend notre alphabet
    # L'idée est de pouvoir retomber sur nos pattes si on dépasse le "z"
    # ou si le décalage nous amène avant le "a"
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    return alphabet[nombre - 1]

# cette fonction reprend les précédentes et chiffre une lettre
def chiffre_une_lettre(lettre, decalage):
    nombre = lettre_vers_nombre(lettre)
    return nombre_vers_lettre(nombre + decalage)


# demander à l'utilisateur ce qu'il veut chiffrer
texte_en_clair = input("texte à chiffrer: ")
decalage = input("decalage: ")

# transformer le décalage en nombre
decalage = int(decalage)

# on initialise le texte chiffré
texte_chiffre = ""

# on parcoure le texte en clair lettre par lettre
# chaque fonction a un nom explicite ce qui rend le code très lisible
for lettre in texte_en_clair:
    lettre = majuscule_vers_minuscule(lettre)
    if doit_etre_chiffre(lettre):
        texte_chiffre = texte_chiffre + chiffre_une_lettre(lettre, decalage)
    else:
        texte_chiffre = texte_chiffre + lettre   

print(texte_chiffre)