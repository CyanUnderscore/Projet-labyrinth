#!/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
util.py : fontions utilitaires pour le projet 2022/2023
          « exploration de labyrinthes avec turtle »

SPDX-FileCopyrightText: 2022 UGA         <francois.puitg@univ-grenoble-alpes.fr>
SPDX-License-Identifier: CC-BY-NC-SA-4.0

Voir l'avis de copyright à la fin de ce fichier.
See copyright notice at the end of this file.
--------------------------------------------------------------------------------
"""


# ----- CODE DE util.py -----

import doctest
import turtle as tt


def labyFromFile(fn) :
    """
    Lecture d'un labyrinthe dans le fichier de nom fn.
    """
    f = open(fn)
    lby = []
    indline = 0
    for fileline in f:
        lbyline = []
        inditem = 0
        for item in fileline:
            if item == "." :         # case vide
                lbyline.append(0)
            elif item == "#" :       # mur
                lbyline.append(1)
            elif item == "x" :       # entrée
                lbyline.append(0)
                mazeIn = [indline, inditem]
            elif item == "X" :       # sortie
                lbyline.append(0)
                mazeOut = [indline, inditem]
            inditem += 1             # discard "\n" char at the end of each line
        lby.append(lbyline)
        indline += 1
    f.close()
    return lby, mazeIn, mazeOut


def lt() :
    """
    Oriente la tortue à +90° vers la gauche.
    """
    tt.lt(90)


def rt() :
    """
    Oriente la tortue à +90° vers la droite.
    """
    tt.rt(90)


def carre(cte, coul='black') :
    """
    Dessine un carré noir (par défaut) de coté cte (pixels).
    Postcondition : stylo sur le coin supérieur droit.
    """
    tt.color(coul)
    tt.begin_fill()
    for _ in range(4) :
        tt.fd(cte) ; rt()
    tt.end_fill()
    tt.fd(cte)                  # coin supérieur droit


def pointille(pnt, dist, coul='black') :
    """
    Trace une ligne pointillée noire (par défaut) de pnt pixels sur une distance
    de dist pixels.
    Postcondition : stylo levé.
    """
    tt.down() ; tt.color(coul)
    for _ in range(int(dist/pnt/2)) :
        tt.fd(pnt) ; tt.up() ; tt.fd(pnt) ; tt.down()
    tt.up()


def pointilles(long, dist, esp, coul='black') :
    """
    Trace des pointillés noir (par défaut) de longueur long sur une distance
    dist espacées de esp.
    """
    pntille=5                 # largeur (en pixel) d'un pointillé
    for _ in range(0, dist, esp) :
        pointille(pntille, long, coul)
        tt.bk(long) ; lt() ; tt.fd(esp) ; rt()


def numerote(dist, ps, coul='black') :
    """
    Numérote (à partir de 0) sur une distance de dist avec un pas de ps
    (dist et ps en pixels).
    """
    tt.pencolor(coul)
    # Lignes :
    for x in range(0, dist, ps) :
        tt.write(x//ps, align="center")
        tt.up() ; tt.fd(ps)


# Angles d'orientation de la tortue pour le déplacement :
ANGLE = {'droite' : 0, 'haut' : 90, 'gauche' : 180, 'bas' : 270}


# Lancement de l'exécution de tous les tests unitaires :
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.FAIL_FAST,
                # https://docs.python.org/fr/3.7/library/doctest.html détaille
                # la signification de optionflags
                # verbose=True
)


# ----- FIN DU CODE DE util.py -----


# Local Variables:
# eval: (setq-default oelu-VC-version "1.0.0")
# End:

# ***************************** AVIS DE COPYRIGHT ******************************
#
#     English translation hereinafter.
#
#     Ce  document est  mis à  disposition sous  LICENCE Creative  Commons
#   « Attribution - Pas d'utilisation commerciale - Partage dans les Mêmes
#   Conditions 4.0 International » (CC BY-NC-SA  4.0) dont les termes sont
#   détaillés  dans  le  fichier  CC-BY-NC-SA-4.0.txt  situé dans le sous-
#   répertoire LICENSES, ou bien sur :
#   http://creativecommons.org/licenses/by-nc-sa/4.0
#
#     Selon  les  conditions  résumées   ci-dessous,  vous  êtes  autorisé
#   à  partager  (copier, distribuer,  communiquer  ce  document par  tous
#   moyens et sous tous formats),  et adapter (remixer, transformer, créer
#   à partir de ce document) :
#     * Attribution : vous devez créditer l'Oeuvre (nom du créateur et des
#     personnes  à attribuer,  notice explicative  des droits  et crédits,
#     notice  de non-responsabilité  et lien  vers l'Oeuvre),  intégrer un
#     lien  vers la  licence  et  indiquer si  des  modifications ont  été
#     effectuées  à  l'Oeuvre  (et   conserver  les  indications  sur  les
#     précédentes modifications). Vous devez indiquer ces informations par
#     tous les moyens raisonnables,  sans toutefois suggérer que l'Offrant
#     vous  soutient ou  soutient  la  façon dont  vous  avez utilisé  son
#     Oeuvre.
#     * Pas d’Utilisation Commerciale  : vous n'êtes pas  autorisé à faire
#     un usage commercial  de cet document, tout ou partie  du matériel le
#     composant.
#     * Partage dans les Mêmes Conditions :  dans le cas où vous effectuez
#     un  remix, que  vous  transformez,  ou créez  à  partir du  matériel
#     composant l'Oeuvre originale, vous  devez diffuser l'Oeuvre modifiée
#     dans les  même conditions, c'est  à dire  avec la même  licence avec
#     laquelle l'Oeuvre originale a été diffusée.
#   Pas  de  restrictions  complémentaires  :  vous  n'êtes  pas  autorisé
#   à  appliquer des  conditions  légales ou  des  mesures techniques  qui
#   restreindraient  légalement  autrui  à   utiliser  l'Oeuvre  dans  les
#   conditions décrites par la licence.
#
#     Notez qu'aucune garantie n'est donnée.  Il se peut que la licence ne
#   vous  donne   pas  toutes  les  permissions   nécessaires  pour  votre
#   utilisation. Par exemple, certains droits  comme les droits moraux, le
#   droit des données personnelles et le droit à l'image sont susceptibles
#   de limiter votre utilisation.
#
#     Le résumé  ci-dessus n'indique  que certaines  des dispositions
#   clé de la licence.  Ce n'est  pas la licence, dont vous auriez dû
#   recevoir une  copie en même  temps que  ce document. Dans  le cas
#   contraire,   l'intégralité  de   la   licence  se   trouve  à   :
#   http://creativecommons.org/licenses/by-nc-sa/4.0
#
# ****************************** COPYRIGHT NOTICE ******************************
#
#     French translation above.
#
#     This document  is LICENSED  under Creative  Commons «  Attribution -
#   NonCommercial - ShareAlike 4.0 International » (CC BY-NC-SA 4.0) whose
#   terms are detailed in the file CC-BY-NC-SA-4.0.txt located in the sub-
#   directory LICENSES, as well as in :
#   http://creativecommons.org/licenses/by-nc-sa/4.0
#
#     Under the  terms and  conditions summarised below,  you are  free to
#   share (copy, redistribute  this document in any medium  or format) and
#   adapt (remix, transform, and build upon this document):
#     * Attribution: you must give appropriate credit (name of the creator
#     and  attribution  parties,  license notice,  disclaimer  notice  and
#     a link to the material), provide a link to the license, and indicate
#     if  changes  were  made  (and   retain  an  indication  of  previous
#     modifications). You may  do so in any reasonable manner,  but not in
#     any way that suggests the licensor endorses you or your use.
#     * NonCommercial:  you  may  not  use  the  material  for  commercial
#     purposes.
#     * ShareAlike: if you  remix, transform, or build  upon the material,
#     you must distribute your contributions under the same license as the
#     original.
#   No  additional  restrictions:  you  may   not  apply  legal  terms  or
#   technological  measures  that  legally   restrict  others  from  doing
#   anything the license permits.
#
#     Note that no warranties are given.  The license may not give you all
#   of  the permissions  necessary for  your intended  use.  For  example,
#   other rights such as publicity, privacy, or moral rights may limit how
#   you use the material.
#
#     The above summary highlights some of the key features and terms
#   of the  actual license.  It is  not the license; you  should have
#   received  a copy  of the  License along  with this  document; you
#   should carefully  review all of  the terms and conditions  of the
#   actual    license   before    using   the    licensed   material:
#   http://creativecommons.org/licenses/by-nc-sa/4.0
#
# ******************************************************************************
