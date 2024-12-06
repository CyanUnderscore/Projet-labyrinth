from deplacements import *
from conversions_et_coordonées import *



def suivreChemin(chemin, dicoJeu):
    '''
    On reçoit une liste de mouvement et on les applique sur la tortue

            Paramétres:
                    chemin(list) : liste de mouvement a executer
                    dicoJeu (dict): base de donné du jeu

    '''
    continuer = True
    for i in chemin:
        if continuer:
            if i=="g":
                continuer = deplacement(-1, 0, dicoJeu, arret_premature=True)
            elif i=="d":
                continuer = deplacement(1, 0, dicoJeu, arret_premature=True)
            elif i=="b":
                continuer = deplacement(0, -1, dicoJeu, arret_premature=True)
            elif i=="h":
                continuer = deplacement(0, 1, dicoJeu, arret_premature=True)
    if continuer:
        print("le chemin a put être executer")
    else:
        print("le chemin n'est pas arriver a son terme (erreur sur la route)")



def inverserChemin(chemin, dicoJeu):
    '''
    On prend une liste de char representant un mouvement et on l'inverse tell que  la tortu fasse le chemin inverse

            Paramétres:
                    chemin(list) : liste de mouvement a inverser
                    dicoJeu (dict): base de donné du jeu
                    

    '''
    chemin_inverse = []
    for elem in range(len(chemin)-1, 0, -1):
        if chemin[elem] == "d":
            chemin_inverse.append("g")
        elif chemin[elem] == "g":
            chemin_inverse.append("d")
        elif chemin[elem] == "h":
            chemin_inverse.append("b")
        elif chemin[elem] == "b":
            chemin_inverse.append("h")
    # pour le dernier mouvement
    elem = 0
    if chemin[elem] == "d":
        chemin_inverse.append("g")
    elif chemin[elem] == "g":
        chemin_inverse.append("d")
    elif chemin[elem] == "h":
        chemin_inverse.append("b")
    elif chemin[elem] == "b":
        chemin_inverse.append("h")
    suivreChemin(chemin_inverse, dicoJeu)



def passage_possible(dicoJeu, cell_turtle, dernier_cell ,dernier_chemin_ignore=True):
    '''
    On obtien la liste des mouvements possible pour la tortue en prenant en compte ou non le dernier mouvement

            Paramétres:
                    dicoJeu (dict): base de donné du jeu
                    cell_turtle (tuple) : position de la tortue en cellule dans le tableau
                    dernier_cell (tuple) : dérniére position de la tortue avant le dernier mouvement
                    dernier_chemin_ignore (bool) : si True le passage d'ou on vient est considerer comme possible si False il ne l'est pas

            Returns:
                    passage (list) : liste de passages possibles
    '''
    passage = []
    if est_mur(cell_turtle[0]+1, cell_turtle[1], dicoJeu)==False and ((cell_turtle[0]+1, cell_turtle[1]) != dernier_cell or dernier_chemin_ignore):
        passage.append("d") 
    if est_mur(cell_turtle[0]-1, cell_turtle[1], dicoJeu)==False and ((cell_turtle[0]-1, cell_turtle[1]) != dernier_cell or dernier_chemin_ignore):
        passage.append("g")
    if est_mur(cell_turtle[0], cell_turtle[1]+1, dicoJeu)==False and ((cell_turtle[0], cell_turtle[1]+1) != dernier_cell or dernier_chemin_ignore):
        passage.append("b")
    if est_mur(cell_turtle[0], cell_turtle[1]-1, dicoJeu)==False and ((cell_turtle[0], cell_turtle[1]-1) != dernier_cell or dernier_chemin_ignore):
        passage.append("h")
    return passage



def emprunte_passage(passage, dicoJeu, chemin):
    '''
    On obtient une direction et on appelle la bonne fonction de mouvement en ajoutant le mouvement a la liste de mouvements.

            Paramétres:
                    passage (str) : mouvement a executer
                    dicoJeu (dict): base de donné du jeu
                    chemin (list): liste de mouvement
    '''
    chemin.append(passage)
    if passage =="d":
        droite(dicoJeu)
    elif passage =="g":
        gauche(dicoJeu)
    elif passage =="b":
        bas(dicoJeu)
    elif passage =="h":
        haut(dicoJeu)

       

def chercher_carrefour(dicoJeu, cell_turtle, dernier_cell, chemins):
    '''
    Cette fonction fait partie de la boucle recursive avec test_branche.
    Si on atteint un carrefour si on est deja passé par ce carrefour il est invalide
    Si aucun des chemin partant du carrefour n'atteignent pas la sortie le carrefour est invalide
    Si une des branches contient un chemin menant vers la sortie le carrefour est valide 
    On appelle test_branche sur chaque branche.

            Paramétres:
                    dicoJeu (dict): base de donné du jeu
                    cell_turtle (tuple) : position de la tortue en cellule dans le tableau
                    dernier_cell (tuple) : dérniére position de la tortue avant le dernier mouvement
                    chemins (list) : different passage possible depuis le carrefour

            Returns:
                    gangne (bool): True si carrefour valide| false si carrefour invalide
                    chemins (list) : vide is carrefour invalide| liste de mouvement de la branche actuelle si carrefour valide
    '''
    cell_carrefour=get_turtle_cell(dicoJeu)
    if list(cell_carrefour) in dicoJeu["carrefour"]:
        return False, []
    dicoJeu["carrefour"].append(list(cell_carrefour))
    for passage in chemins:
        chemin_branche = []
        cell_turtle = tuple(cell_carrefour)
        emprunte_passage(passage, dicoJeu, chemin_branche)
        print("chemin branche ", chemin_branche)
        dernier_cell = tuple(cell_carrefour)    
        cell_turtle = get_turtle_cell(dicoJeu)
        
        gagnant , chemin_branche_gagnante = test_branche(dicoJeu, cell_turtle, dernier_cell, chemin_branche)
        if gagnant == True:
            return True, chemin_branche_gagnante
    return False, []
            


def test_branche(dicoJeu, cell_turtle, dernier_cell, chemin_branche):
    '''
    Cette fonction fait partie de la boucle recursive avec chercher_carrefour.
    La tortue navigue vers la fin de la branche désigner par l'emplacement actuelle de la tortue et celui d'avants.
    Si elle atteint une impasse le passage est invalide.
    Si le passage ateint la sortie le passage est valide.
    Si le passage ateint un carrefour on appelle chercher_carrefour.

            Paramétres:
                    dicoJeu (dict): base de donné du jeu
                    cell_turtle (tuple) : position de la tortue en cellule dans le tableau
                    dernier_cell (tuple) : dérniére position de la tortue avant le dernier mouvement
                    chemin_branche (list) : liste de mouvement de la branche actuelle

            Returns:
                    gangne (bool): True si chemin valide| false si chemin invalide
                    chemin_branche (list) : vide is chemin invalide| liste de mouvement de la branche actuelle si chemin valide
    '''
    print(typeCellule(cell_turtle[1], cell_turtle[0], dicoJeu))
    while typeCellule(cell_turtle[1], cell_turtle[0], dicoJeu) != "carrefour" and typeCellule(cell_turtle[1], cell_turtle[0], dicoJeu) != "sortie" and typeCellule(cell_turtle[1], cell_turtle[0], dicoJeu) != "impasse":
        if typeCellule(cell_turtle[1], cell_turtle[0], dicoJeu) == "entre":
            passage = passage_possible(dicoJeu, cell_turtle, dernier_cell, True)[0] # si passage standart alors 1 elem
            dernier_cell = tuple(cell_turtle)                    
            emprunte_passage(passage, dicoJeu, chemin_branche)
            cell_turtle = get_turtle_cell(dicoJeu)
        else:
            passage = passage_possible(dicoJeu, cell_turtle, dernier_cell, False)[0] # si passage standart alors 1 elem
            dernier_cell = tuple(cell_turtle)      
            emprunte_passage(passage, dicoJeu, chemin_branche)
            cell_turtle = get_turtle_cell(dicoJeu)

    if typeCellule(cell_turtle[1], cell_turtle[0], dicoJeu) == "sortie":
        return True, chemin_branche
    
    elif typeCellule(cell_turtle[1], cell_turtle[0], dicoJeu) == "impasse":
        inverserChemin(chemin_branche, dicoJeu)
        return False, []

    elif typeCellule(cell_turtle[1], cell_turtle[0], dicoJeu) == "carrefour":
        gagnant , chemin_carrefour = chercher_carrefour(dicoJeu, cell_turtle, dernier_cell, passage_possible(dicoJeu, cell_turtle, dernier_cell, False))
        if gagnant == True:
            chemin_branche+=chemin_carrefour
            return True, chemin_branche
        inverserChemin(chemin_branche, dicoJeu)
        return False, []
        
    
    
def explorer(dicoJeu):
    '''
    Lance l'exploration et affiche si la tortue peut atteindre la sortie et si c'est le cas affiche le chemin venant a la victoir qui sera verifié a l'envers et a lendroit.

            Paramétres:
                    dicoJeu (dict): base de donné du jeu
    '''
    cell_turtle = get_turtle_cell(dicoJeu)
    dernier_cell = cell_turtle
    gagné, chemin_victoir = test_branche(dicoJeu, cell_turtle, dernier_cell, [])
    if gagné:
        print(chemin_victoir)
        print("Vérificatouion du chemin ")
        inverserChemin(chemin_victoir, dicoJeu)
        suivreChemin(chemin_victoir, dicoJeu)
        print("victoir")
    else:
        print("la tortue ne peux pas atteindre la sortie")
