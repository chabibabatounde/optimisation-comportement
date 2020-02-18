
# coding: utf-8
from Modules import Solution as mdSolution
Solution = mdSolution.Solution 
import random
import json
import pandas as pd
import matplotlib.pyplot as pltl

class Immunitaire:
    nbAnticorps = 0 
    maxIterration = 0 
    proportion = 0
    systemeImm =  []

    def __init__(self, probleme, maxIterration, nbAnticorps, proportion):
        self.maxIterration = maxIterration
        self.nbAnticorps = nbAnticorps
        self.probleme = probleme
        self.proportion = proportion
        print "Algorithme Immunitaire instancié"

    def optimiser(self):
        print "Optimisation en cours..."
        output = []

        #Géneration aléatoire de la population et evaluation de chaque individu
        while len(self.systemeImm) < self.nbAnticorps:
            self.systemeImm.append(self.probleme.genererIndividu())

        self.systemeImm = sorted(self.systemeImm, key=lambda solution:solution.fitness)
        iterration = 0
        #Démarrage du processus ittératif
        while iterration < self.maxIterration:
            self.clonnage()
            self.systemeImm = sorted(self.systemeImm, key=lambda solution:solution.fitness)
            self.systemeImm =  self.systemeImm[:self.nbAnticorps]
            iterration =  iterration + 1
            print("\tItérration "+str(iterration)+" :  Meilleur fitness = "+str(self.systemeImm[0].fitness))
            output.append({"iterration":iterration, "fitness":self.systemeImm[0].fitness})

        self.performance(output)
        return self.systemeImm[0]

    def performance(self, data):
        calcul1x = []
        calcul1y = []
        optix = []
        optiy = []
        
        for ligne in data:
            calcul1x.append(ligne['fitness'])
            calcul1y.append(ligne['iterration'])
            optix.append(0)
            optiy.append(ligne['iterration'])
        pltl.plot(calcul1y, calcul1x, label="Solution obtenue")
        pltl.plot(optiy, optix, label='Solution reelle')
        pltl.legend()
        pltl.savefig('Courbe de performance.png', dpi=500)

    def clonnage(self):
        nombre = int(round(self.proportion * self.nbAnticorps/100))
        for anticorps in self.systemeImm[:nombre]:
            nbClonnage = self.nbClonnage(anticorps)
            for i in range(0, nbClonnage):
                if(nbClonnage<10):
                    self.systemeImm.append(self.muter(anticorps))
                else:
                    self.systemeImm.append(self.hypermuter(anticorps))

    def nbClonnage(self, anticorps):
        in_min  = 0
        in_max  = 50000
        out_min  = 0
        out_max  = 20
        return int(round((anticorps.fitness - in_min) * (out_max - out_min) / (in_max - in_min) + out_min))

    def codageReel(self, parent):
        adn = [parent.vecteur1[0], parent.vecteur1[1], parent.vecteur1[2], parent.vecteur2[0], parent.vecteur2[1], parent.vecteur3[2], parent.vecteur3[0], parent.vecteur3[1], parent.vecteur3[2], parent.vecteur4[0], parent.vecteur4[1], parent.vecteur4[2], parent.vecteur5[0], parent.vecteur5[1], parent.vecteur5[2],parent.mass,parent.energie]
        return adn
        
    def hypermuter(self, anticorps):
        adn =  self.codageReel(anticorps)
        for point in range(0, len(adn)):
            positif = random.randint(0,1)
            valeur = random.uniform(10, 100)
            if(positif==1):
                adn[point] = adn[point]+valeur
            else:
                adn[point] = adn[point]-valeur
        mutant = Solution([adn[0],adn[1],adn[2]],[adn[3],adn[4],adn[5]],[adn[6],adn[7],adn[8]],[adn[9],adn[10],adn[11]],[adn[12],adn[13],adn[14]],adn[15],adn[16])
        mutant = self.probleme.evaluerIndividu(mutant)
        return mutant
    
    def muter(self, anticorps):
        adn =  self.codageReel(anticorps)
        for point in range(0, len(adn)):
            positif = random.randint(0,1)
            valeur = random.uniform(0, 10)
            if(positif==1):
                adn[point] = adn[point]+valeur
            else:
                adn[point] = adn[point]-valeur
        mutant = Solution([adn[0],adn[1],adn[2]],[adn[3],adn[4],adn[5]],[adn[6],adn[7],adn[8]],[adn[9],adn[10],adn[11]],[adn[12],adn[13],adn[14]],adn[15],adn[16])
        mutant = self.probleme.evaluerIndividu(mutant)
        return mutant