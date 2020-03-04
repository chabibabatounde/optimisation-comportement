# coding: utf-8

class Agent:
    mass = 0
    energie = 0

    def __init__(self, mass, energie, comportement):
        self.mass = mass
        self.comportement = comportement
        self.energie = energie

    def run(self, executionTime):
        return self.comportement.exprimer(self, executionTime)
        