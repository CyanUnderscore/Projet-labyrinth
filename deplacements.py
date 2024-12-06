import turtle
from conversions_et_coordonées import pixel2cell
from type import est_mur, typeCellule


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


