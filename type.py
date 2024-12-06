
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
        
