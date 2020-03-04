# coding: utf-8
import json
import numpy as np

class Errance:
    def __init__(self, vecteur1, vecteur2, vecteur3, vecteur4, vecteur5):
        self.vecteur1 = vecteur1
        self.vecteur2 = vecteur2
        self.vecteur3 = vecteur3
        self.vecteur4 = vecteur4
        self.vecteur5 = vecteur5

    def exprimer(self,agent,executionTime):
        return self.fonctionComportementale(agent,executionTime)

    def fonctionComportementale(self,agent,executionTime):
        x = 0.0
        y = 0.0
        z = 0.0
        output = []
        theta = np.linspace(-4 * np.pi, 4 * np.pi, executionTime+1)
        for time in range(0,executionTime) :
            if agent.energie >= 0.7:
                if time >= 0 and time < 20:
                    x = x + self.vecteur1[0] + (agent.energie/100) - (agent.mass/10)
                    y = y + 25 * (self.vecteur1[1] + (agent.energie/100) - (agent.mass/10))
                    z = 3 * self.vecteur1[2] * np.sin(time)
                    agent.energie = agent.energie - 3.3

                if time >= 20 and time < 40:
                    x = x - self.vecteur2[0] - (agent.energie/100) + (agent.mass/100)
                    y = y - self.vecteur2[1] - (agent.energie/100) + (agent.mass/100)
                    z = z + self.vecteur2[2]
                    agent.energie = agent.energie + 1.9
                    
                if time >= 40 and time < 60:
                    x = agent.energie * self.vecteur3[0] * np.cos(theta[time])
                    y = agent.energie * self.vecteur3[1] * np.sin(theta[time])
                    z = z - self.vecteur3[2]
                    agent.energie = agent.energie - 0.3

                if time >= 60 and time < 80:
                    x = agent.energie * self.vecteur4[0] * np.cos(theta[time])
                    y = agent.energie * self.vecteur4[1] * np.sin(theta[time])
                    z = z + self.vecteur4[2] 
                    agent.energie = agent.energie - (agent.mass/10)

                if time >= 80 and time < 100:
                    x = agent.energie * self.vecteur5[0] * np.cos(theta[time])
                    y = agent.energie * self.vecteur5[1] * np.sin(theta[time])
                    z = z + self.vecteur5[2] 
                    agent.energie = agent.energie + 5.9
                    
            output.append({"x":x, "y":y, "z":z, "iterration" :time, "mass":agent.mass, "energie":agent.energie})
            if (time == 24):
                agent.energie = agent.energie + 24
        output = json.dumps(output)
        return (output)
