# # #Question 3.1
def nbMotsAvecVoyelle(nomf):
    voyelles = ['a', 'e', 'i', 'o', 'u']
    count = 0

    with open(nomf, 'r') as file:
        for line in file:
            word = line.strip()
            if word[0] in voyelles:
                count += 1

    return count
# Appel de la fonction nbMotsAvecVoyelle
nomf = "C:/Users/Kebe Sakhir/Desktop/Examen Python yade/Partie3/fichier.txt" 
resultat_nb_mots = nbMotsAvecVoyelle(nomf)
print(f"Nombre de mots commençant par une voyelle : {resultat_nb_mots}")




# # Question 3.2

def compterChaqueMot(nomf1, nomf2):
    previous_word = ''
    count = 0

    with open(nomf1, 'r') as input_file, open(nomf2, 'w') as output_file:
        for line in input_file:
            word = line.strip()
            if word != previous_word:
                if count > 0:
                    output_file.write(f"{previous_word} {count}\n")
                previous_word = word
                count = 1
            else:
                count += 1

       
        if count > 0:
            output_file.write(f"{previous_word} {count}\n")
#Appel de la procédure compterChaqueMot
nomf1 = "C:/Users/Kebe Sakhir/Desktop/Examen Python yade/Partie3/fichier.txt"  
nomf2 = "C:/Users/Kebe Sakhir/Desktop/Examen Python yade/Partie3/nom_fichier2.txt"  
compterChaqueMot(nomf1, nomf2)
print(" Comptage  avec succès.")
            

