# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Modules import Simulateur as mdSimulateur
Simulateur = mdSimulateur.Simulateur 


class Graphique:
    def __init__(self, solution, titre):
        simulateur = Simulateur()
        resultat = simulateur.generate(solution)
        x = []
        y = []
        z = []
        for ligne in resultat:
            x.append(ligne['x'])
            y.append(ligne['y'])
            z.append(ligne['z'])
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(x, y, z, label=titre)
        ax.legend()
        plt.savefig(titre+'.png', dpi=500)
        plt.clf()
