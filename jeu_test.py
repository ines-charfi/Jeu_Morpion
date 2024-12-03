import random

# Initialisation de la grille de jeu (vide au début)
Grille = ["-" ,"-" ,"-", 
          "-" ,"-" ,"-", 
          "-" ,"-", "-"]

# Variables globales pour suivre l'état du jeu
joueur_actuel = ""  # Le joueur actuel ("X" ou "O")
fin_jeu = False  # Indique si la partie est terminée
contre_bot = False  # Indique si on joue contre un bot
niveau_bot = ""  # Niveau du bot : "facile" ou "difficile"


# Fonction principale du jeu
def jouer():
    """
    Cette fonction gère le cycle complet du jeu :
    - Réinitialisation de la grille pour chaque nouvelle partie.
    - Choix du mode de jeu (contre un joueur ou un bot).
    - Gestion des tours et affichage du résultat.
    """
    global Grille, fin_jeu
    while True:
        Grille = ["-"] * 9  # Réinitialisation de la grille
        fin_jeu = False  # Réinitialisation de l'état du jeu
        choix_mode()  # Permet de choisir entre jouer contre un joueur ou un bot
        if contre_bot:
            choix_niveau_bot()  # Si contre un bot, choisir le niveau
        choix_joueur()  # Le joueur choisit s'il joue X ou O
       

        # Boucle principale du jeu
        while not fin_jeu:
            tour(joueur_actuel)  # Gérer le tour du joueur ou du bot
            affichage_grille() #affichage grille après un tour complet
            verifier_fin_jeu()  # Vérifier si le jeu est terminé (gagnant ou nul)
            if not fin_jeu:
                joueur_suivant()  # Passer au joueur suivant si la partie continue

        # Demander si les joueurs veulent rejouer
        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if rejouer != "o":
            print("Merci d'avoir joué ! À bientôt !")
            break  # Quitter la boucle si les joueurs ne veulent plus jouer


# Fonction pour choisir le mode de jeu
def choix_mode():
    """
    Permet de choisir si on joue contre un autre joueur ou contre un bot.
    Modifie la variable globale `contre_bot`.
    """
    global contre_bot
    choix = input("Voulez-vous jouer contre un bot ? (o/n) : ").lower()
    contre_bot = choix == "o"  # True si l'utilisateur choisit de jouer contre un bot


# Fonction pour choisir le niveau du bot
def choix_niveau_bot():
    """
    Permet de choisir le niveau de difficulté du bot : facile ou difficile.
    Modifie la variable globale `niveau_bot`.
    """
    global niveau_bot
    while True:
        niveau_bot = input("Choisissez le niveau du bot : facile ou difficile (f/d) : ").lower()
        if niveau_bot in ["f", "d"]:
            niveau_bot = "facile" if niveau_bot == "f" else "difficile"
            print(f"Vous avez choisi un bot {niveau_bot}.")
            break
        else:
            print("Entrée invalide. Veuillez choisir entre 'f' (facile) ou 'd' (difficile).")


# Fonction pour choisir le premier joueur
def choix_joueur():
    """
    Permet à l'utilisateur de choisir son symbole (X ou O).
    Si le joueur choisit X, l'autre joueur ou le bot prendra O, et vice-versa.
    """
    global joueur_actuel
    while True:
        joueur_actuel = input("Veuillez choisir votre signe, soit une croix (X), soit un rond (O) : ").upper()
        if joueur_actuel == 'X':
            print("Vous avez choisi X. L'autre joueur/bot prendra O.")
            break
        elif joueur_actuel == 'O':
            print("Vous avez choisi O. L'autre joueur/bot prendra X.")
            break
        else:
            print("Entrée invalide. Veuillez choisir entre X et O.")


# Fonction pour afficher la grille
def affichage_grille():
    """
    Affiche l'état actuel de la grille ainsi que les numéros de cases
    pour aider les joueurs à choisir leur position.
    """
    print("\n")
    print("-------------")
    print(f"| {Grille[0]} | {Grille[1]} | {Grille[2]} |                           |1|2|3|")
    print(f"| {Grille[3]} | {Grille[4]} | {Grille[5]} |                           |4|5|6|")
    print(f"| {Grille[6]} | {Grille[7]} | {Grille[8]} |                           |7|8|9|")
    print("-------------")
    print("\n")


# Fonction pour gérer le tour du joueur ou du bot
def tour(joueur):
    """
    Gère le tour du joueur actuel :
    - Si c'est le bot, effectue un coup en fonction de son niveau.
    - Si c'est un joueur humain, demande une position valide.
    """
    global contre_bot, niveau_bot
    if joueur == "O" and contre_bot:  # Si c'est le tour du bot
        print("Le bot joue...")
        if niveau_bot == "facile":
            bot_facile()
        elif niveau_bot == "difficile":
            bot_kenza_difficile()
    else:  # Si c'est le tour d'un joueur humain
        print(f"C'est le tour du joueur : {joueur}")
        valide = False
        while not valide:
            try:
                # Demander une position entre 1 et 9
                position = int(input("Veuillez sélectionner une case vide sur la grille entre 1 et 9 : ")) - 1
                # Vérifier si la position est valide
                if position in range(9) and Grille[position] == "-":
                    Grille[position] = joueur
                    valide = True
                else:
                    print("Case invalide ou déjà occupée. Veuillez réessayer.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entre 1 et 9.")
    


# Fonction pour vérifier la fin du jeu
def verifier_fin_jeu():
    """
    Vérifie si le joueur actuel a gagné ou si la grille est pleine (match nul).
    Met fin à la partie si l'une de ces conditions est remplie.
    """
    global fin_jeu
    if coup_gagnant(joueur_actuel):  # Vérifie si le joueur actuel a une combinaison gagnante
        print(f"Félicitations ! Le joueur {joueur_actuel} a gagné !")
        fin_jeu = True
    elif "-" not in Grille:  # Vérifie si toutes les cases sont remplies (match nul)
        print("Match nul !")
        fin_jeu = True


# Fonction pour vérifier si un joueur a une combinaison gagnante
def coup_gagnant(joueur):
    """
    Vérifie si un joueur a une combinaison gagnante parmi les lignes,
    colonnes ou diagonales.
    """
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combinaison in combinaisons_gagnantes:
        if Grille[combinaison[0]] == Grille[combinaison[1]] == Grille[combinaison[2]] == joueur:
            return True
    return False


# Fonction pour changer de joueur
def joueur_suivant():
    """
    Change le joueur actuel :
    - Si c'est "X", passe à "O".
    - Si c'est "O", passe à "X".
    """
    global joueur_actuel
    joueur_actuel = "O" if joueur_actuel == "X" else "X"


# Bot facile : joue sur une case libre au hasard
def bot_facile():
    """
    Bot de niveau facile :
    - Choisit une case libre au hasard.
    """
    position_vide = [i for i, case in enumerate(Grille) if case == "-"]
    if position_vide:
        Grille[random.choice(position_vide)] = "O"


# Bot difficile (Kenbot)
def bot_kenza_difficile():
    """
    Kenbot joue intelligemment :
    - Cherche à gagner si possible.
    - Bloque l'adversaire si nécessaire.
    - Sinon, joue sur une case libre aléatoire.
    """
    global Grille

    def trouver_meilleur_coup(joueur):
        """
        Vérifie les meilleures positions pour gagner ou bloquer.
        """
        #boucle pour parcourir ttes les combinaisons gagnantes possibles
        for combinaison in [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]:
            #extraire les valeurs dans la grille pour combinaiser
            #ex si combinaison [0,1,2] donne ligne 1 grille
            valeurs = [Grille[i] for i in combinaison]

            #vérifier si cette combinaison a exactement:
            #deux cases remplies par le joueur actuel(valeur.count(joueur))
            #une seule case remplie encore vide(valeurs.count("-" ==1))
            if valeurs.count(joueur) == 2 and valeurs.count("-") == 1:
                #si cette condition est vraie, retourner à l'index de la case vide dans la combinaison de la case vide dans valeurs
                #on utilise cette position poour retrouver l'index dans la  grille principale avec 'combinaison'
                return combinaison[valeurs.index("-")]
            #si aucune combinaison ne correspond, retourner none
        return None

    # Kenbot essaie de gagner
    coup = trouver_meilleur_coup("O")
    if coup is not None:
        Grille[coup] = "O"
        return

    # Kenbot essaie de bloquer l'adversaire
    coup = trouver_meilleur_coup("X")
    if coup is not None:
        Grille[coup] = "O"
        return

    # Sinon, joue sur une case libre aléatoire
    position_vide = [i for i, case in enumerate(Grille) if case == "-"]
    if position_vide:
        Grille[random.choice(position_vide)] = "O"


# Lancer le jeu
jouer()
