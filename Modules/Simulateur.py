# coding: utf-8
from Agent import *
from Errance import *
import json

class Simulateur:
    def simuler(self, solution):
        comportement = Errance(solution.vecteur1,solution.vecteur2,solution.vecteur3,solution.vecteur4,solution.vecteur5)
        agent = Agent(solution.mass, solution.energie, comportement)
        result = agent.run(100)
        #print(result)
        data =  json.loads(result)
        return data