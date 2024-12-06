import turtle


def afficheTextuel(laby_tableau, dicoJeu):
    '''
    On affiche une représentation graphique du tableau dans la console.

            Paramétres:
                    laby_tableau(list): tableau du labyrinthe
                    dicoJeu (dict): base de donné du jeu
    '''
    for index_liste in range(len(laby_tableau)):
        ligne = ""
        for index_elem in range(len(laby_tableau[index_liste])):
            if laby_tableau[index_liste][index_elem] == 0:
                if [index_liste, index_elem] == dicoJeu["entre"]:
                    ligne+="x"
                elif [index_liste, index_elem] == dicoJeu["sortie"]:
                    ligne+="o"
                else:
                    ligne+=" "
            elif laby_tableau[index_liste][index_elem] == 1:
                ligne+="#"
        print(ligne)



def affichageGraphique(laby_tableau, dicoJeu):
    '''
    On affiche une représentation graphique du tableau dans une fenétre grace a trurtle.

            Paramétres:
                    laby_tableau(list): tableau du labyrinthe
                    dicoJeu (dict): base de donné du jeu
    '''
    curseur = dicoJeu["curseur"]
    curseur.speed(0)
    turtle.clear()
    turtle.tracer(0) #on desactive les mise a jour de l'écran pour voir instrantanément les changement
    epaisseur = dicoJeu["epaisseur"]
    depart = dicoJeu["depart"] #point superieur gauche
    for y_index in range(len(laby_tableau)):
        
        curseur.up()
        curseur.goto(depart[0], depart[1]-epaisseur*y_index)
        curseur.down()

        for x_index in range(len(laby_tableau[y_index])):
            couleur =""
            if laby_tableau[y_index][x_index]==1:
                couleur = "grey"
            elif [y_index, x_index] == dicoJeu["entre"]:
                couleur = "blue"
            elif [y_index, x_index] == dicoJeu["sortie"]:
                couleur = "red"
            elif typeCellule(y_index, x_index, dicoJeu)=="carrefour":
                couleur = "green"
            if couleur != "": # si couleur == "" alors la case est vide on ne trace donc rien
                curseur.fillcolor(couleur)
                curseur.begin_fill()
                for i in range(4):
                    curseur.forward(epaisseur)
                    curseur.left(90)
                curseur.end_fill()
            curseur.up()
            curseur.forward(epaisseur)
            curseur.down()
    turtle.update() # on fait la mise a jour car on la desac plus tot
    turtle.tracer(1)



def pixel2cell(x_global, y_global, dicoJeu):
    '''
    On determine la place de la tortue dans le tableau a partir de sa position dans la fenétre.

            Paramétres:
                    x_global (int) : position en x donné par turtle.x_cor
                    y_global (int) : position en y donné par turtle.y_cor
                    dicoJeu (dict): base de donné du jeu


            Returns:
                    (tuple) : tuple renvois (colonne, ligne)
    '''
    
    #local (dans le dessin du tableau (on deplace l'origine))
    x_local = x_global-dicoJeu["depart"][0]
    y_local = y_global-dicoJeu["depart"][1]
    for y_index in range(len(dicoJeu["laby_tableau"])):
        for x_index in range(len(dicoJeu["laby_tableau"][y_index])):
            epaisseur = dicoJeu["epaisseur"]
            if x_index*epaisseur<x_local<(x_index+1)*epaisseur and -y_index*epaisseur<y_local<-(y_index-1)*epaisseur :
                return (x_index, y_index)



def cell2pixel(x_tableau, y_tableau, dicoJeu):
    '''
    On determine la place de la tortue dans la fenétre a partir de sa position dans le tableau.

            Paramétres:
                    x_tableau (int) : position en x dans le tableau
                    y_tableau (int) : position en y dans le tableau
                    dicoJeu (dict): base de donné du jeu


            Returns:
                    (tuple) : tuple renvois (x, y)
    '''
    x_local = dicoJeu["epaisseur"] * (x_tableau +0.5) # +0.5 pour ếtre au millieu de la case 
    y_local = dicoJeu["epaisseur"] * -(y_tableau -0.5)
    x_global = x_local+dicoJeu["depart"][0]
    y_global = y_local+dicoJeu["depart"][1]
    return x_global, y_global



def testClic(x,y, dicoJeu):
    coordonate = pixel2cell(x, y, dicoJeu)
    if coordonate ==None:
        print("erreur hors de tableau")
    else:
        print("colone", coordonate[0], "ligne", coordonate[1])
        print(x, y)
        print(cell2pixel( coordonate[0], coordonate[1], dicoJeu))



def est_mur(colonne, ligne, dicoJeu):
    '''
    Renvois si la case a analyser est un mur

            Paramétres:
                    ligne (int) : ligne de la cellule ananlyser
                    colonne (int) : colonne de la ligne a analyser
                    dicoJeu (dict): base de donné du jeu

            Returns:
                    (bool) True->(mur ou en dehors du tableau) False->(case valide pour deplacement)
    '''
    if ligne==None or colonne==None:
        return True
    if 0<=ligne<=len(dicoJeu["laby_tableau"])-1 and 0<=colonne<=len(dicoJeu["laby_tableau"][0])-1:
        if dicoJeu["laby_tableau"][ligne][colonne] == 1:
            return True
        return False
    return True



def typeCellule(ligne, colonne, dicoJeu):
    '''
    Renvois le type de la cellule
            Paramétres:
                    ligne (int) : ligne de la cellule ananlyser
                    colonne (int) : colonne de la ligne a analyser
                    dicoJeu (dict): base de donné du jeu


            Returns:
                    (str) : type de le cellule
    '''
    if dicoJeu["laby_tableau"][ligne][colonne] == 1:
        return "mur"
    if dicoJeu["entre"]==[ligne, colonne]:
        return "entre"
    if dicoJeu["sortie"]==[ligne, colonne]:
        return "sortie"
    else:
        mur = 0
#y
        if est_mur(colonne+1, ligne, dicoJeu):
            mur+=1
        if est_mur(colonne-1, ligne, dicoJeu):
            mur+=1
        if est_mur(colonne, ligne+1, dicoJeu):
            mur+=1
        if est_mur(colonne, ligne-1, dicoJeu):
            mur+=1


        if mur ==3:
            return "impasse"
        if mur==2:
            return "passage standard"
        if mur <=1:
            return "carrefour"
        


def get_turtle_cell(dicoJeu):
    '''
    Renvois la position de la tortue dans le tableau

            Paramétres:
                    dicoJeu (dict): base de donné du jeu

            Returns:
                   (tuple) : position de la tortue dans le tableau
    '''
    return pixel2cell(turtle.xcor(), turtle.ycor(), dicoJeu)



def deplacement(x, y, dicoJeu, arret_premature=False):
    '''
    Cette fontion est a l'orignine de tous les déplacement de la tortue et change sa couleur en fonction de la case sur laquelle elle se positionne

            Paramétres:
                    x: coef de modification de la position de la tortue en x
                    y: coef de modification de la position de la tortue en y
                    dicoJeu (dict): base de donné du jeu
                    arret_premature(bool): demande de renvoyer un bool si la case a laquel on veut acceder est un mur

            Returns:
                    si arret_premature=True:
                        valide (bool) : le passage est il valide ? True(on ce deplace sur une case valide) /False(on ce deplace sur un mur)
    '''
    pixel_pos = pixel2cell(turtle.xcor()+x*dicoJeu["epaisseur"], turtle.ycor()+y*dicoJeu["epaisseur"], dicoJeu)
    if pixel_pos==None:
        turtle.color("red")
    
    elif est_mur(pixel_pos[0],pixel_pos[1], dicoJeu):
        turtle.color("red")
        print("les murs c'est dur")
        if arret_premature : return False
    
    elif dicoJeu["sortie"]==[pixel_pos[1],pixel_pos[0]]:
        turtle.color("green")
        turtle.goto(turtle.xcor()+x*dicoJeu["epaisseur"], turtle.ycor()+y*dicoJeu["epaisseur"])

    elif typeCellule(pixel_pos[1],pixel_pos[0], dicoJeu)=="impasse":
        turtle.color("orange")
        turtle.goto(turtle.xcor()+x*dicoJeu["epaisseur"], turtle.ycor()+y*dicoJeu["epaisseur"])
    
    elif typeCellule(pixel_pos[1],pixel_pos[0], dicoJeu)=="carrefour":
        turtle.color("blue")
        turtle.goto(turtle.xcor()+x*dicoJeu["epaisseur"], turtle.ycor()+y*dicoJeu["epaisseur"])
    
    else:
        turtle.color("black")
        turtle.goto(turtle.xcor()+x*dicoJeu["epaisseur"], turtle.ycor()+y*dicoJeu["epaisseur"])

    if arret_premature : return True



def gauche(dicoJeu):
    deplacement(-1, 0, dicoJeu)
    turtle.setheading(180)
    


def droite(dicoJeu):
    deplacement(1, 0, dicoJeu)
    turtle.setheading(0)



def bas(dicoJeu):
    deplacement(0, -1, dicoJeu)
    turtle.setheading(-90)



def haut(dicoJeu): 
    deplacement(0, 1, dicoJeu)
    turtle.setheading(90)



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
            


def test_branche(dicoJeu, cell_turtle, dernier_cell, chemin_branche) -> (bool, list[str]):
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

