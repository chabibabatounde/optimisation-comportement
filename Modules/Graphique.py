# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Modules import Simulateur as mdSimulateur
Simulateur = mdSimulateur.Simulateur 


class Graphique:
    def multiple(self, solution1, titre1, solution2, titre2):
        simulateur = Simulateur()
        resultat = simulateur.simuler(solution1)
        x = []
        y = []
        z = []
        for ligne in resultat:
            x.append(ligne['x'])
            y.append(ligne['y'])
            z.append(ligne['z'])
        xx = []
        yy = []
        zz = []
        resultat = simulateur.simuler(solution2)
        for ligne in resultat:
            xx.append(ligne['x'])
            yy.append(ligne['y'])
            zz.append(ligne['z'])
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.plot(x, y, z, label=titre1)
        ax.plot(xx, yy, zz, label=titre2)

        ax.legend()
        plt.savefig(titre1+titre2+'.png', dpi=500)
        plt.clf()




    def single(self, solution, titre):
        simulateur = Simulateur()
        resultat = simulateur.simuler(solution)
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
