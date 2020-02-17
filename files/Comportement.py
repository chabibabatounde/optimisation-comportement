# coding: utf-8
import json
import numpy as np

class Comportement:
    def __init__(self, vecteur1, vecteur2, vecteur3, vecteur4, vecteur5):
        self.vecteur1 = vecteur1
        self.vecteur2 = vecteur2
        self.vecteur3 = vecteur3
        self.vecteur4 = vecteur4
        self.vecteur5 = vecteur5
    def action(self,agent,executionTime):
        clock = 0
        x = 0.0
        y = 0.0
        z = 0.0
        output = []
        theta = np.linspace(-4 * np.pi, 4 * np.pi, executionTime+1)
        for time in range(0,executionTime) :
            if agent.energie >= 0.7:
                if clock >= 6 and clock < 8:
                    x = x + self.vecteur1[0] + (agent.energie/100) - (agent.mass/100)
                    y = y + self.vecteur1[1] + (agent.energie/100) - (agent.mass/100)
                    z = z + self.vecteur1[2] + (agent.energie/100) - (agent.mass/100)
                    agent.energie = agent.energie - 0.3
                if clock >= 8 and clock < 12:
                    x = agent.energie * self.vecteur2[0] * np.cos(theta[time])
                    y = agent.energie * self.vecteur2[1] * np.sin(theta[time])
                    z = z - self.vecteur2[2] + (agent.energie/100)
                    agent.energie = agent.energie - 2.2
                if clock >= 12 and clock < 15:
                    x = agent.energie * self.vecteur3[0] * np.cos(theta[time])
                    y = agent.energie * self.vecteur3[1] * np.sin(theta[time])
                    z = z + self.vecteur3[2] - (agent.energie/100)
                    agent.energie = agent.energie - 1.9
                if clock >= 15 and clock < 20:
                    x = x + self.vecteur4[0] + (agent.energie/100) - (agent.mass/100)
                    y = y + self.vecteur4[1] + (agent.energie/100) - (agent.mass/100)
                    z = z + self.vecteur4[2]
                    agent.energie = agent.energie - 0.7
                if (clock >= 20 and clock <= 23) or (clock >= 0 and clock < 6):
                    x = agent.energie * self.vecteur5[0] * np.cos(theta[time])
                    y = agent.energie * self.vecteur5[1] * np.sin(theta[time])
                    z = z + 0.001
                    agent.energie = agent.energie - 0.8
            output.append({"x":x, "y":y, "z":z, "iterration" :time, "clock":clock, "energie":agent.energie})
            clock = clock+1
            if (clock == 24):
                agent.energie = agent.energie + 24
                clock =0
        output = json.dumps(output)
        return (output)
