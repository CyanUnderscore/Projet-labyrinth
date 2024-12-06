import turtle
from type import typeCellule

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

