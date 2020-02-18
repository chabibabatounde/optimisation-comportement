# coding: utf-8
from Genetique.AlgoGenetique import * 
from Immunitaire.Immunitaire import * 
from Modules.Probleme import * 
from Modules.Graphique import * 

#Probleme d'origine
#solutionDeBase = Solution([1.0,0.9,0.2], [2.0,1.0,0.7], [2.5,3.8,-0.1], [1.2,-2.2,-3.3], [0.1,-0.4,0.01],20.0, 80.0)
#solutionDeBase = Solution([1.0,0.9,0.2], [2.0,1.0,0.7], [2.5,3.8,0.1], [1.2,2.2,3.3], [0.1,0.4,0.01],20.0, 80.0)
solutionDeBase = Solution([1.0,0.9,0.2], [2.0,1.0,0.1], [2.5,3.8,1.1], [1.2,2.2,0.455], [0.1,0.6,0.35],20.0, 80.0)
Graphique(solutionDeBase, "Comportement connu")

#Création d'une instance de probleme d'optimisation
probleme = Probleme("input.json")

#Création d'une instance de l'algo d'optimisation
#algorithme = AlgoGenetique(probleme= probleme, maxIterration=5, taillePopulation=1000, nombreCroisement=20)
algorithme = Immunitaire(probleme= probleme, maxIterration=2500,  proportion=60, nbAnticorps=1000)

#Lancement du calcul
resultats = algorithme.optimiser()
#Affichage du Résultat
Graphique(resultats, "Comportement obtenu")
resultats.decrire()