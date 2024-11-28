from lireLaby import labyFromFile
from fonction import (explorer, haut, bas, gauche, droite ,suivreChemin, inverserChemin,afficheTextuel,deplacement, affichageGraphique, pixel2cell, testClic, cell2pixel, est_mur, typeCellule) 
import turtle
#1.1
nom_du_fichier = "laby2024/labys/"+input("entrer le nom du fichier contennant le labyrinthe : ")+".laby"
laby_tableau, laby_entre, laby_sortie = labyFromFile(nom_du_fichier)

EXPLORATION = "explorztion"
EDITION = "edition"

#affichage
for liste in laby_tableau:
    print(liste)
print("entrée :", laby_entre)
print("sortie :", laby_sortie)

#création dicojeu
dicoJeu= {}
dicoJeu["mode"] = EXPLORATION
dicoJeu["entre"] = laby_entre
dicoJeu["sortie"] = laby_sortie
dicoJeu["epaisseur"] = 50
dicoJeu["depart"] = [-400, 200]
dicoJeu["laby_tableau"] = laby_tableau
dicoJeu["chemin"] = []
dicoJeu["carrefour"] = []

afficheTextuel(laby_tableau, dicoJeu)


curseur =turtle.Turtle()
dicoJeu["curseur"] = curseur
affichageGraphique(laby_tableau, dicoJeu)
print(pixel2cell(-153, -10, dicoJeu))

def testClicForOnScreenClick(x, y): #si on a pas cette fonction on ne peut pas passer dicoJeu a testClic() dans onscreenclick()
    testClic(x, y, dicoJeu)

turtle.up()
def gauche_input():
    gauche(dicoJeu)
    dicoJeu["chemin"].append("g")
    print(dicoJeu["chemin"])

def droite_input():
    droite(dicoJeu)
    dicoJeu["chemin"].append("d")
    print(dicoJeu["chemin"])

def bas_input():
    bas(dicoJeu)
    dicoJeu["chemin"].append("b")
    print(dicoJeu["chemin"])

def haut_input(): 
    haut(dicoJeu)
    dicoJeu["chemin"].append("h")
    print(dicoJeu["chemin"])

def explorer_input():
    explorer(dicoJeu)

def testChemin():
    print(dicoJeu["chemin"])
    inverserChemin(dicoJeu)
    suivreChemin(dicoJeu["chemin"], dicoJeu)



CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

def draw_onclick(x, y):
    turtle.dot(100, 'cyan')

turtle.onkeypress(gauche_input,"q")
turtle.onkeypress(droite_input,"d")
turtle.onkeypress(haut_input,"z")
turtle.onkeypress(bas_input,"s")
turtle.onkeypress(testChemin, "t")
turtle.onkeypress(explorer_input, "e")
turtle.speed(0)
turtle.listen()

turtle.goto(cell2pixel(dicoJeu["entre"][1],dicoJeu["entre"][0], dicoJeu ))
turtle.mainloop()
