import turtle

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


def get_turtle_cell(dicoJeu):
    '''
    Renvois la position de la tortue dans le tableau

            Paramétres:
                    dicoJeu (dict): base de donné du jeu

            Returns:
                   (tuple) : position de la tortue dans le tableau
    '''
    return pixel2cell(turtle.xcor(), turtle.ycor(), dicoJeu)

