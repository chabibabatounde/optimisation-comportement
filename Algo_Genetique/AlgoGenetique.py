# coding: utf-8
from Modules import Solution as mdSolution
Solution = mdSolution.Solution 
import random
import json
import pandas as pd
import matplotlib.pyplot as pltl

class AlgoGenetique:
    taillePopulation = 0 
    maxIterration = 0 
    nombreCroisement = 0 
    population =  []

    def __init__(self, probleme, maxIterration, taillePopulation, nombreCroisement):
        self.maxIterration = maxIterration
        self.taillePopulation = taillePopulation
        self.nombreCroisement = nombreCroisement
        self.probleme = probleme
        print "Algorithme Génétique instancié"
        
    def optimiser(self):
        
        print "Optimisation en cours..."
        output = []
        #Géneration aléatoire de la population et evaluation de chaque individu
        while len(self.population) < self.taillePopulation:
            self.population.append(self.probleme.genererIndividu())
        
        iterration = 0
        while iterration < self.maxIterration:
            iterration =  iterration + 1


            #Methode de selection II      
            for croisement in range(0,self.taillePopulation/100*self.nombreCroisement):
                #trie de la population
                self.population = sorted(self.population, key=lambda solution:solution.fitness)
                #Selection des parents
                
                parent1 = self.population[random.randint(0, self.taillePopulation-1)]
                parent2 = self.population[random.randint(0, self.taillePopulation-1)]
                #Croissement
                enfant1, enfant2 = self.croiser(parent1, parent2)
                enfant1.generation =  iterration + 1
                enfant2.generation =  iterration + 1
                self.population.append(enfant1)
                self.population.append(enfant2)
                self.population.append(self.mutationReel(enfant1))
                self.population.append(self.mutationReel(enfant2))
            #Normalisation
            self.population =  self.population[:self.taillePopulation]


            print("\tItérration "+str(iterration)+" :  Meilleur fitness = "+str(self.population[0].fitness))
            output.append({"iterration":iterration, "fitness":self.population[0].fitness})



        print "Optimisation Terminé"
        self.performance(output)

        return self.population[0]

    def loisNormale(self, parent1, parent2):
        proportion = random.uniform(0, 1)
        adnParent1 = self.codageReel(parent1)
        adnParent2 = self.codageReel(parent2)
        vecteur1 =  [((proportion*adnParent1[0]) + ((1-proportion)*adnParent2[0])),((proportion*adnParent1[1]) + ((1-proportion)*adnParent2[1])),((proportion*adnParent1[2]) + ((1-proportion)*adnParent2[2]))]
        vecteur2 =  [((proportion*adnParent1[3]) + ((1-proportion)*adnParent2[3])),((proportion*adnParent1[4]) + ((1-proportion)*adnParent2[4])),((proportion*adnParent1[5]) + ((1-proportion)*adnParent2[5]))]
        vecteur3 =  [((proportion*adnParent1[6]) + ((1-proportion)*adnParent2[6])),((proportion*adnParent1[7]) + ((1-proportion)*adnParent2[7])),((proportion*adnParent1[8]) + ((1-proportion)*adnParent2[8]))]
        vecteur4 =  [((proportion*adnParent1[9]) + ((1-proportion)*adnParent2[9])),((proportion*adnParent1[10]) + ((1-proportion)*adnParent2[10])),((proportion*adnParent1[11]) + ((1-proportion)*adnParent2[11]))]
        vecteur5 =  [((proportion*adnParent1[12]) + ((1-proportion)*adnParent2[12])),((proportion*adnParent1[13]) + ((1-proportion)*adnParent2[13])),((proportion*adnParent1[14]) + ((1-proportion)*adnParent2[14]))]
        mass =  ((proportion*adnParent1[15]) + ((1-proportion)*adnParent2[15]))
        energie =  ((proportion*adnParent1[16]) + ((1-proportion)*adnParent2[16]))
        enfant1 =  Solution(vecteur1,vecteur2,vecteur3,vecteur4,vecteur5,mass,energie)
        enfant1 = self.probleme.evaluerIndividu(enfant1)

        vecteur1 =  [((proportion*adnParent2[0]) + ((1-proportion)*adnParent1[0])),((proportion*adnParent2[1]) + ((1-proportion)*adnParent1[1])),((proportion*adnParent2[2]) + ((1-proportion)*adnParent1[2]))]
        vecteur2 =  [((proportion*adnParent2[3]) + ((1-proportion)*adnParent1[3])),((proportion*adnParent2[4]) + ((1-proportion)*adnParent1[4])),((proportion*adnParent2[5]) + ((1-proportion)*adnParent1[5]))]
        vecteur3 =  [((proportion*adnParent2[6]) + ((1-proportion)*adnParent1[6])),((proportion*adnParent2[7]) + ((1-proportion)*adnParent1[7])),((proportion*adnParent2[8]) + ((1-proportion)*adnParent1[8]))]
        vecteur4 =  [((proportion*adnParent2[9]) + ((1-proportion)*adnParent1[9])),((proportion*adnParent2[10]) + ((1-proportion)*adnParent1[10])),((proportion*adnParent2[11]) + ((1-proportion)*adnParent1[11]))]
        vecteur5 =  [((proportion*adnParent2[12]) + ((1-proportion)*adnParent1[12])),((proportion*adnParent2[13]) + ((1-proportion)*adnParent1[13])),((proportion*adnParent2[14]) + ((1-proportion)*adnParent1[14]))]
        mass =  ((proportion*adnParent2[15]) + ((1-proportion)*adnParent1[15]))
        energie =  ((proportion*adnParent2[16]) + ((1-proportion)*adnParent1[16]))
        enfant2 =  Solution(vecteur1,vecteur2,vecteur3,vecteur4,vecteur5,mass,energie)
        enfant2 = self.probleme.evaluerIndividu(enfant2)

        return enfant1, enfant2

    def croiser(self, parent1, parent2):
        #return self.loisNormale(parent1, parent2)
        return self.croisementReel(parent1, parent2)

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
    

    def mutationReel(self, solution):
        adn = self.codageReel(solution)
        #definir le nombre de mutation
        nbMutation = random.randint(0,8)
        #definir les points de crossing over
        listDesPoints = []
        index = 0
        for i in range(0,nbMutation):
            listDesPoints.append(random.randint(0,8))
            listDesPoints.sort()

        for point in listDesPoints:
            positif = random.randint(0,1)
            valeur = random.uniform(0,10)
            if(positif==1):
                adn[point] = adn[point]+valeur
            else:
                adn[point] = adn[point]-valeur
        
        #Un seul point de mutation
        '''
        positif = random.randint(0,1)
        valeur = random.uniform(0, 10)
        point = random.randint(0,16)
        if(positif==1):
            adn[point] = adn[point]+valeur
        else:
            adn[point] = adn[point]-valeur'''


        mutant = Solution([adn[0],adn[1],adn[2]],[adn[3],adn[4],adn[5]],[adn[6],adn[7],adn[8]],[adn[9],adn[10],adn[11]],[adn[12],adn[13],adn[14]],adn[15],adn[16])
        mutant = self.probleme.evaluerIndividu(mutant)
        return mutant

    def codageReel(self, parent):
        adn = [parent.vecteur1[0], parent.vecteur1[1], parent.vecteur1[2], parent.vecteur2[0], parent.vecteur2[1], parent.vecteur3[2], parent.vecteur3[0], parent.vecteur3[1], parent.vecteur3[2], parent.vecteur4[0], parent.vecteur4[1], parent.vecteur4[2], parent.vecteur5[0], parent.vecteur5[1], parent.vecteur5[2],parent.mass,parent.energie]
        return adn
    

    def croisementReel(self, parent1, parent2):
        adnParent1 = self.codageReel(parent1)
        adnParent2 = self.codageReel(parent2)
        adnEnfant1 = []
        adnEnfant2 = []
        #definir le nombre de crossing over
        nbCrossing = random.randint(1,16)
        #definir les points de crossing over
        listDesPoints = []
        index = 0
        for i in range(0,nbCrossing):
            listDesPoints.append(random.randint(1,16))
            listDesPoints.sort()

        for i in listDesPoints:
            if(index==0):
                for j in range(0,i):
                    adnEnfant1.append(adnParent1[j])
                    adnEnfant2.append(adnParent2[j])
            else:
                for k in range(listDesPoints[index-1], i):
                    if(index%2==0):
                        adnEnfant1.append(adnParent1[k])
                        adnEnfant2.append(adnParent2[k])
                    else:
                        adnEnfant1.append(adnParent2[k])
                        adnEnfant2.append(adnParent1[k])
            index = index + 1

        for n in range(listDesPoints[nbCrossing-1], len(adnParent1)):
                if(index%2==0):
                    adnEnfant1.append(adnParent1[n])
                    adnEnfant2.append(adnParent2[n])
                else:
                    adnEnfant1.append(adnParent2[n])
                    adnEnfant2.append(adnParent1[n])

        enfant1 = Solution([adnEnfant1[0],adnEnfant1[1],adnEnfant1[2]],[adnEnfant1[3],adnEnfant1[4],adnEnfant1[5]],[adnEnfant1[6],adnEnfant1[7],adnEnfant1[8]],[adnEnfant1[9],adnEnfant1[10],adnEnfant1[11]],[adnEnfant1[12],adnEnfant1[13],adnEnfant1[14]],adnEnfant1[15],adnEnfant1[16])
        enfant2 = Solution([adnEnfant2[0],adnEnfant2[1],adnEnfant2[2]],[adnEnfant2[3],adnEnfant2[4],adnEnfant2[5]],[adnEnfant2[6],adnEnfant2[7],adnEnfant2[8]],[adnEnfant2[9],adnEnfant2[10],adnEnfant2[11]],[adnEnfant2[12],adnEnfant2[13],adnEnfant2[14]],adnEnfant2[15],adnEnfant2[16])
        enfant1 = self.probleme.evaluerIndividu(enfant1)
        enfant2 = self.probleme.evaluerIndividu(enfant2)
        return enfant1, enfant2

    def croisementBinaire(self, parent1, parent2):
        return parent1, parent2