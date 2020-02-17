from Agent import *
from Comportement import *
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import json

comportement = Comportement([1.0,0.9,0.2], [2.0,1.0,0.7], [2.5,3.8,-0.1], [1.2,-2.2,-3.3], [0.1,-0.4,0.01])
agent = Agent(20.0, 80.0, comportement)
agent.decrire()
data =  json.loads(agent.run(100))

x = []
y = []
z = []

for ligne in data:
    x.append(ligne['x'])
    y.append(ligne['y'])
    z.append(ligne['z'])

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')


ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()