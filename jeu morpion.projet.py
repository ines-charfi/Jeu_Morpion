Grille =["-" ,"-" ,"-" ,
         "-" ,"-" ,"-" ,
         "-" ,"-", "-" ]

joueur_actuel = ""
fin_jeu = False
#definition jouer()
def jouer():
    
    choix_joueur()
    affichage_grille()
    while fin_jeu == False :
        tour(joueur_actuel)
        verifier_fin_jeu()
        joueur_suivant()
       
#definition de la fonction choix_joueur
def choix_joueur():
    global joueur_actuel
    joueur_actuel = input("Veuillez choisir votre signe soit une croix (X), soit un rond(O) : ")
    while True :
        joueur_actuel = joueur_actuel.upper()
        if joueur_actuel == 'X' :
            print(" vous avez choisi X. Le joueur n° 2 prendra O ")
           
        elif joueur_actuel == 'O':
            print("Vous avez choisi O; Le joueur n° 2 prendra X ")
    
    else:
    joueur_actuel = input("Veuillez choisir votre signe soit une croix (X), soit un rond(O) : ")
        
#definition de la fonction affichage_grille
def affichage_grille() :
    print("\n")
    print("-------------")
    print("|", Grille[0] , "|" , Grille[1] , "|" , Grille[2],  "|                           |1|2|3|")  
    print("|", Grille[3] , "|" , Grille[4] , "|" , Grille[5] , "|                           |4|5|6|")
    print("|", Grille[6] , "|" , Grille[7] , "|" , Grille[8] , "|                           |7|8|9|")
    print("-------------")
    print("\n")
#definition de la fonction tour(joueur)
def tour(joueur) :
    print("c'est le tour de joueur :  ", joueur)  
    position = input("Veuillez séléctionner un espace vide sur la grille entre 1 et 9 :  ")
    valide = False
    while valide == False :
        while position not in ["1", "2", "3", "4", "5", "6," "7", "8", "9"] :
            position = input("Veuillez séléctionner un espace vide sur la grille entre 1 et 9 :  ")
            position = int(position-1)
    
        if Grille[position] == "-" :
            valide = True
        else:
            print(" Vous ne pouvez pas accéder à cette case")
    Grille[position] = joueur
affichage_grille()
 #definition de la fonction verifier_fin_jeu
def verifier_fin_jeu():
  verifier_victoire()
  verifier_match_nul()
#definition de la fonction verifier_victoire()
def verifier_victoire():
    global fin_jeu
    global gagant
    
    if Grille[0] == Grille[1] == Grille[2] and Grille[2] != "-":
        fin_jeu == True
        gagant = Grille[1]
    if Grille[3] == Grille[4] == Grille[5] and Grille[5] != "-":
        fin_jeu == True
        gagant = Grille[2]
    if Grille[6] == Grille[7] == Grille[8] and Grille[8] != "-":
        fin_jeu == True
        gagant = Grille[8]
    if Grille[6] == Grille[7] == Grille[8] and Grille[8] != "-":
         fin_jeu == True
         gagant = Grille[8]
    if Grille[1] == Grille[4] == Grille[7] and Grille[7] != "-":
        fin_jeu == True
        gagant = Grille[7]
    if Grille[2] == Grille[5] == Grille[8] and Grille[8] != "-":
        fin_jeu == True
        gagant = Grille[8]
    if Grille[0] == Grille[4] == Grille[8] and Grille[8] != "-":
        fin_jeu == True
        gagant = Grille[8]
    if Grille[2] == Grille[4] == Grille[6] and Grille[6] != "-":
        fin_jeu == True
        gagant = Grille[6]
#definition de l fonction verifier_match_nul
def verifier_match_nul():
    global fin_jeu
    if "_" not in Grille:
        fin_jeu = True
        
def joueur_suivant():
    global joueur_actuel
    if joueur_actuel == 'X':
        joueur_suivant ='O'
    else:
        joueur_actuel = "O"
        joueur_suivant = "X"
        
        jouer()
    
        
        
    
        
        
        
                