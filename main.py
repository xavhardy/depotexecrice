
# exercice 3 liste 1

def multiple_3_5(p_nombre):
    """

    :param p_nombre: le nombre a tester
    :return: 1 si multiple de 3,2 si multiple 5,3 si multiple, de 3 et 5 et 0
    si n'est pas multiple de 3 et 5
    """
    if p_nombre % 3 == 0:
        if p_nombre % 5 == 0:
            return 3
        else:
            return 1
    elif p_nombre % 5 == 0:
        return 2
    else:
        return 0


# programe principale
try:
    nbr = int(input("Entrer un nombre "))
    if nbr == 0:
        print("entrer un nombre sictement positif...")
    # traitement
    résultat = multiple_3_5(nbr)
    print("le résulat:", résultat)

# sortie de données : affichage
except ValueError:
    print("entrer un nombre positif")
else:
    if résultat == 1:
        print("le nombre est un multiple de trois")
    elif résultat == 2:
        print("le nombre entre est un multiple de 5 ")
    elif résultat == 3:
        print("le nomre entre est un multiple de 5 et de 3")
    else:
        print("le nombre entre est ni un multiple de 3 ni de 5")
