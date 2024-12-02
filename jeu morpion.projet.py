Grille = ["-" ,"-" ,"-", 
          "-" ,"-" ,"-", 
          "-" ,"-", "-"]

joueur_actuel = ""
fin_jeu = False

# Fonction principale du jeu
def jouer():
    global Grille, fin_jeu  # Pour réinitialiser la grille et l'état du jeu
    while True:  # Boucle principale pour rejouer
        Grille = ["-"] * 9  # Réinitialisation de la grille
        fin_jeu = False  # Réinitialisation de l'état du jeu
        choix_joueur()
        affichage_grille()
        while not fin_jeu:
            tour(joueur_actuel)
            verifier_fin_jeu()
            if not fin_jeu:
                joueur_suivant()
        # Demander si les joueurs veulent rejouer
        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if rejouer != "o":
            print("Merci d'avoir joué ! À bientôt !")
            break  # Quitter la boucle si les joueurs ne veulent

# Fonction pour choisir le joueur initial
def choix_joueur():
    global joueur_actuel
    while True:
        joueur_actuel = input("Veuillez choisir votre signe, soit une croix (X), soit un rond (O) : ").upper()
        if joueur_actuel == 'X':
            print("Vous avez choisi X. Le joueur n°2 prendra O.")
            break
        elif joueur_actuel == 'O':
            print("Vous avez choisi O. Le joueur n°2 prendra X.")
            break
        else:
            print("Entrée invalide. Veuillez choisir entre X et O.")

# Fonction pour afficher la grille
def affichage_grille():
    print("\n")
    print("-------------")
    print(f"| {Grille[0]} | {Grille[1]} | {Grille[2]} |                           |1|2|3|")
    print(f"| {Grille[3]} | {Grille[4]} | {Grille[5]} |                           |4|5|6|")
    print(f"| {Grille[6]} | {Grille[7]} | {Grille[8]} |                           |7|8|9|")
    print("-------------")
    print("\n")

# Fonction pour gérer le tour d'un joueur
def tour(joueur):
    print(f"C'est le tour du joueur : {joueur}")
    valide = False
    while not valide:
        try:
            position = int(input("Veuillez sélectionner une case vide sur la grille entre 1 et 9 : ")) - 1
            if position in range(9) and Grille[position] == "-":
                Grille[position] = joueur
                valide = True
            else:
                print("Case invalide ou déjà occupée. Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 9.")
    affichage_grille()

# Fonction pour vérifier la fin du jeu
def verifier_fin_jeu():
    global fin_jeu
    if coup_gagnant(joueur_actuel):
        print(f"Félicitations ! Le joueur {joueur_actuel} a gagné !")
        fin_jeu = True
    elif "-" not in Grille:
        print("Match nul !")
        fin_jeu = True

# Fonction pour vérifier si un joueur a une combinaison gagnante
def coup_gagnant(joueur):
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combo in combinaisons_gagnantes:
        if Grille[combo[0]] == Grille[combo[1]] == Grille[combo[2]] == joueur:
            return True

# Fonction pour changer de joueur
def joueur_suivant():
    global joueur_actuel
    joueur_actuel = "O" if joueur_actuel == "X" else "X"

# Lancer le jeu
jouer()
