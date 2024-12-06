import turtle
from conversions_et_coordonées import pixel2cell, cell2pixel

def testClic(x,y, dicoJeu):
    coordonate = pixel2cell(x, y, dicoJeu)
    if coordonate ==None:
        print("erreur hors de tableau")
    else:
        print("colone", coordonate[0], "ligne", coordonate[1])
        print(x, y)
        print(cell2pixel( coordonate[0], coordonate[1], dicoJeu))



    '''
    Renvois la position de la tortue dans le tableau

            Paramétres:
                    dicoJeu (dict): base de donné du jeu

            Returns:
                   (tuple) : position de la tortue dans le tableau
    '''
    return pixel2cell(turtle.xcor(), turtle.ycor(), dicoJeu)




