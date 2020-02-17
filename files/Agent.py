# coding: utf-8

class Agent:
    mass = 0
    energie = 0

    def __init__(self, mass, energie, comportement):
        self.mass = mass
        self.comportement = comportement
        self.energie = energie
        print("Nouvel agent créé")

    def decrire(self):
        print "L'agent a une masse de", self.mass,"a une energie =", self.energie

    def run(self, executionTime):
        return self.comportement.action(self, executionTime)
        