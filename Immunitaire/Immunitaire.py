
# coding: utf-8
from Modules import Solution as mdSolution
Solution = mdSolution.Solution 
import random
import json
import pandas as pd
import matplotlib.pyplot as pltl

class Immunitaire:
    taillePopulation = 0 
    maxIterration = 0 
    population =  []

    def __init__(self, probleme, maxIterration, taillePopulation, nombreCroisement):
        self.maxIterration = maxIterration
        self.taillePopulation = taillePopulation
        self.nombreCroisement = nombreCroisement
        self.probleme = probleme
        print "Algorithme Génétique instancié"

    def optimiser(self):

        print("OK")