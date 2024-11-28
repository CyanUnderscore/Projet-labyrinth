# Lire un labyrinthe dans un fichier et le renvoyer au format liste
# Read a maze from a file and return it as a list
def labyFromFile(fn):
	f = open(fn)
	laby = []
	indline = 0
	for fileline in f:
		labyline = []
		inditem = 0
		for item in fileline:
			# empty cell / case vide
			if item == ".":
				labyline.append(0)
			# wall / mur
			elif item == "#":
				labyline.append(1)
			# entrance / entree
			elif item == "x":
				labyline.append(0)
				mazeIn = [indline,inditem]
			# exit / sortie
			elif item == "X":
				labyline.append(0)
				mazeOut = [indline,inditem]
			# discard "\n" char at the end of each line
			inditem += 1
		laby.append(labyline)
		indline += 1
	f.close()
	return laby, mazeIn, mazeOut