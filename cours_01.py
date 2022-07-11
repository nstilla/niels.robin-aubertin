# ceci est un commentaire
# une variable peut contenir une valeur
mon_nom = "Niels"
# cette valeur peut être un entier
mon_age = 31
# on peut concaténer des chaines de caractères avec l'opérateur "+"
print("Bonjour " + mon_nom + " et j'ai " + str(mon_age) + " ans.")
# on peut créer une chaine de caratères "formatée" avec f""
a_afficher = f"Bonjour {mon_nom} et j'ai {mon_age + 1} ans."
# on peut afficher une variable
print(a_afficher)

# ma première fonction !
def vieillir(age):
    return age + 1

# afficher 11
print(vieillir(10))
# stocker mon age + 1 an
mon_age_dans_un_an = vieillir(mon_age)
# afficher la valeur stockée dans la variable "mon_age_dans_un_an"
print(mon_age_dans_un_an)