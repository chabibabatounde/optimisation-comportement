# coding: utf-8
import json
from Comportement import * 

class Solution:

    def __init__(self, vecteur1, vecteur2, vecteur3, vecteur4, vecteur5, mass, energie):
        self.vecteur1 = vecteur1
        self.vecteur2 = vecteur2
        self.vecteur3 = vecteur3
        self.vecteur4 = vecteur4
        self.vecteur5 = vecteur5
        self.mass = mass
        self.energie = energie
        self.generation = 1
        self.comportement = Comportement(vecteur1,vecteur2,vecteur3,vecteur4,vecteur5)

    def decrire(self):
        print(self.vecteur1, self.vecteur2, self.vecteur3, self.vecteur4, self.vecteur5, self.mass, self.energie, self.fitness, "Gen", self.generation)