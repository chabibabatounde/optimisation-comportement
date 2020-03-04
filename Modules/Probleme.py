# coding: utf-8
import json
import random 
from Solution import * 
from Simulateur import *


class Probleme:
    dataSet = "[]"

    def __init__(self, dataSetPath):
        with open(dataSetPath, 'r') as f:
            self.dataSet = json.load(f)
        print "Probleme instancié"

    def genererIndividu(self):
        vecteur1 = [random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)]
        vecteur2 = [random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)]
        vecteur3 = [random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)]
        vecteur4 = [random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)]
        vecteur5 = [random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)]
        solution = Solution(vecteur1, vecteur2, vecteur3, vecteur4, vecteur5, random.uniform(0, 10), random.uniform(0, 200))
        self.evaluerIndividu(solution)
        return solution

    def evaluerIndividu(self, solution):
        simulateur = Simulateur()
        resultat = simulateur.simuler(solution)
        solution.fitness = 0
        for i in range(0, len(self.dataSet)-1):
            genere =  resultat[i]
            reel =  self.dataSet[i]
            solution.fitness =  solution.fitness + abs(reel['energie']- genere['energie'])+ abs(reel['x']- genere['x']) + abs(reel['y']- genere['y']) + abs(reel['z']- genere['z']) 
        return solution    