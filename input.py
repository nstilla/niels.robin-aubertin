# On peut demander à l'utilisateur d'entrer une valeur
# Le programme va stopper et redémarrer quand l'utilisateur validera son entrée
reponse = input("Quel est votre âge ? ")

# Une valeur de retour d'input est toujours une string (chaine de caractères)
# ici, on veut transformer le résultat en entier
age = int(reponse)

# utiliser age comme un entier nous permet de faire des opérations dessus
print(f"Dans 10 ans, vous aurez {age + 10} ans")