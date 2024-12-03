import random

# Codes ANSI pour les couleurs
ROUGE = "\033[91m"  # Pour X
VERT = "\033[92m"   # Pour O
BLEU = "\033[94m"   # Pour les messages
MAGENTA = "\033[35m"  # Pour les messages
JAUNE = "\033[93m"  # Pour le bot
RESET = "\033[0m"  # Réinitialiser la couleur

# Initialisation de la grille de jeu (vide au début)
Grille = ["-" ,"-" ,"-", 
          "-" ,"-" ,"-", 
          "-" ,"-", "-"]

# Variables globales pour suivre l'état du jeu
joueur_actuel = ""  # Le joueur actuel ("X" ou "O")
fin_jeu = False  # Indique si la partie est terminée
contre_bot = False  # Indique si on joue contre un bot

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
        choix_joueur()  # Le joueur choisit s'il joue X ou O
        affichage_grille()  # Afficher la grille au début de la partie

        # Boucle principale du jeu
        while not fin_jeu:
            tour(joueur_actuel)  # Gérer le tour du joueur ou du bot
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

# Fonction pour choisir le joueur initial
def choix_joueur():
    """
    Permet à l'utilisateur de choisir son symbole (X ou O).
    Si le joueur choisit X, l'autre joueur ou le bot prendra O, et vice-versa.
    """
    global joueur_actuel
    while True:
        joueur_actuel = input(f"{MAGENTA}Veuillez choisir votre signe, soit une croix (X), soit un rond (O) : {RESET}").upper()
        if joueur_actuel == 'X':
            print(f"{VERT}Vous avez choisi X. L'autre joueur/bot prendra O.{RESET}")
            break
        elif joueur_actuel == 'O':
            print(f"{BLEU}Vous avez choisi O. L'autre joueur/bot prendra X.{RESET}")
            break
        else:
            print(f"{ROUGE}Entrée invalide. Veuillez choisir entre X et O.{RESET}")

# Fonction pour afficher la grille
def affichage_grille():
    """
    Affiche l'état actuel de la grille ainsi que les numéros de cases
    pour aider les joueurs à choisir leur position.
    """
    print("\n")
    print("-------------")
    print(f"| {ROUGE}{Grille[0]} | {ROUGE}{Grille[1]} | {ROUGE}{Grille[2]} |                            |1|2|3|")
    print(f"| {VERT}{Grille[3]} | {VERT}{Grille[4]} | {VERT}{Grille[5]} |                            |4|5|6|")
    print(f"| {ROUGE}{Grille[6]} | {VERT}{Grille[7]} | {ROUGE}{Grille[8]} |                            |7|8|9|")
    print("-------------")
    print("\n")

# Fonction pour gérer le tour d'un joueur ou du bot
def tour(joueur):
    """
    Gère le tour du joueur actuel :
    - Si c'est le bot, effectue un coup aléatoire.
    - Si c'est un joueur humain, demande une position valide.
    """
    global contre_bot
    if joueur == "O" and contre_bot:  # Si c'est le tour du bot
        print(f"{JAUNE}Le bot joue...{RESET}")
        bot_mouvement_random()
    else:  # Si c'est le tour d'un joueur humain
        if joueur == "X":
            joueur_color = ROUGE
        else:
            joueur_color = VERT
        print(f"{joueur_color}C'est le tour du joueur : {joueur}{RESET}")
        valide = False
        while not valide:
            try:
                # Demander une position entre 1 et 9
                position = int(input(f"{BLEU}Veuillez sélectionner une case vide sur la grille entre 1 et 9 : {RESET}")) - 1
                # Vérifier si la position est valide
                if position in range(9) and Grille[position] == "-":
                    Grille[position] = joueur
                    valide = True
                else:
                    print(f"{JAUNE}Case invalide ou déjà occupée. Veuillez réessayer.{RESET}")
            except ValueError:
                print(f"{JAUNE}Entrée invalide. Veuillez entrer un nombre entre 1 et 9.{RESET}")
    affichage_grille()

# Fonction pour vérifier la fin du jeu
def verifier_fin_jeu():
    """
    Vérifie si le joueur actuel a gagné ou si la grille est pleine (match nul).
    Met fin à la partie si l'une de ces conditions est remplie.
    """
    global fin_jeu
    if coup_gagnant(joueur_actuel):  # Vérifie si le joueur actuel a une combinaison gagnante
        print(f"{VERT}Félicitations ! Le joueur {joueur_actuel} a gagné !{RESET}")
        fin_jeu = True
    elif "-" not in Grille:  # Vérifie si toutes les cases sont remplies (match nul)
        print(f"{JAUNE}Match nul !{RESET}")
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

# Fonction pour gérer le coup aléatoire du bot
def bot_mouvement_random():
    """
    Le bot joue un coup en choisissant une position vide aléatoire
    dans la grille.
    """
    global Grille
    position_vide = [i for i, cellule in enumerate(Grille) if cellule == "-"]

    if position_vide:
        position = random.choice(position_vide)
        Grille[position] = "O"  # Le bot joue toujours "O"

# Lancer le jeu
jouer()