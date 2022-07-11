# exemple de correction de l'exercice de l acomptine avec le cours 01
def comptine(km):
    return f"{km} km à pied, ça use les souliers"

print(comptine(1))
print(comptine(2))
print(comptine(3))

# exemple avec les boucles while et for du cours 02
i = 0
ma_comptine = []
while i < 3:
    i = i + 1
    # on stocke chage vers généré dans la list ma_comptine
    ma_comptine.append(comptine(i))

# On affiche maintenant les vers stockés sous forme de liste
for vers in ma_comptine:
    print(vers)