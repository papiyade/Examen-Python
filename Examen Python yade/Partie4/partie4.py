# Question 1


def Saisie():
    t = []
    while True:
        nom = input("Entrez le nom de la personne (ou 'q' pour quitter) : ")
        if nom.lower() == 'q':
            break
        t.append(nom)
    return t

# Exemple d'utilisation
personnes = Saisie()
print(personnes)

# Question 2
