
#Définissons d'abord la classe Personne
class Personne:
    def __init__(self, nom, prenom, numero_rue, nom_rue, numero_telephone, code_postal, ville):
        self.nom = nom
        self.prenom = prenom
        self.numero_rue = numero_rue
        self.nom_rue = nom_rue
        self.numero_telephone = numero_telephone
        self.code_postal = code_postal
        self.ville = ville

# Fonction pour  saisir les données de l'annuaire
def saisie_tab():
    annuaire = []
    print("Ajoutez des personnes")
    while True:
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        numero_rue = input("Numéro dans la rue : ")
        nom_rue = input("Nom de la rue : ")
        numero_telephone = input("Numéro de téléphone : ")
        code_postal = input("Code postal : ")
        ville = input("Ville : ")

        personne = Personne(nom, prenom, numero_rue, nom_rue, numero_telephone, code_postal, ville)
        annuaire.append(personne)

        choix = input("Voulez-vous ajouter une autre personne à l'annuaire ? (O/N) ")
        if choix.upper() == 'N':
            break
    
    return annuaire

# Fonction pour choisir le critère de recherche
def critere_recherche():
    critere = input("Choisir le critère de recherche (nom, prénom, nom de la rue, numéro de téléphone, code postal, ville) : ")
    return critere.lower()

# Fonction de recherche
def recherche(annuaire, critere):
    valeur_recherche = input(f"Entrez la valeur de recherche pour le critère '{critere}' : ")
    resultat = []

    for personne in annuaire:
        if critere == 'nom' and personne.nom.lower() == valeur_recherche.lower():
            resultat.append(True)
        elif critere == 'prénom' and personne.prenom.lower() == valeur_recherche.lower():
            resultat.append(True)
        elif critere == 'nom de la rue' and personne.nom_rue.lower() == valeur_recherche.lower():
            resultat.append(True)
        elif critere == 'numéro de téléphone' and personne.numero_telephone == valeur_recherche:
            resultat.append(True)
        elif critere == 'code postal' and personne.code_postal == valeur_recherche:
            resultat.append(True)
        elif critere == 'ville' and personne.ville.lower() == valeur_recherche.lower():
            resultat.append(True)
        else:
            resultat.append(False)
    
    return resultat

# Procédure pour afficher les informations des personnes correspondant à la recherche
def affiche_tab(annuaire, resultat_recherche):
    print("Résultat de la recherche :")
    for personne, resultat in zip(annuaire, resultat_recherche):
        if resultat:
            print(f"Nom : {personne.nom}")
            print(f"Prénom : {personne.prenom}")
            print(f"Numéro dans la rue : {personne.numero_rue}")
            print(f"Nom de la rue : {personne.nom_rue}")
            print(f"Numéro de téléphone : {personne.numero_telephone}")
            print(f"Code postal : {personne.code_postal}")
            print(f"Ville : {personne.ville}")
            print()

# Programme principal
annuaire = saisie_tab()

critere = critere_recherche()

resultat_recherche = recherche(annuaire, critere)

affiche_tab(annuaire, resultat_recherche)

   