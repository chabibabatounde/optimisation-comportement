# coding: utf-8
from Genetique.AlgoGenetique import * 
from Modules.Probleme import * 
from Modules.Graphique import * 
#solutionDeBase = Solution([1.0,0.9,0.2], [2.0,1.0,0.7], [2.5,3.8,-0.1], [1.2,-2.2,-3.3], [0.1,-0.4,0.01],20.0, 80.0)
solutionDeBase = Solution([1.0,0.9,0.2], [2.0,1.0,0.1], [2.5,3.8,1.1], [1.2,2.2,0.455], [0.1,0.6,0.35],20.0, 80.0)
Graphique(solutionDeBase, "Comportement test")