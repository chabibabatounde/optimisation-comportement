from Agent import *
from Comportement import *
import json

def generate():
    comportement = Comportement([1.0,0.9,0.2], [2.0,1.0,0.7], [2.5,3.8,-0.1], [1.2,-2.2,-3.3], [0.1,-0.4,0.01])
    agent = Agent(20.0, 80.0, comportement)
    agent.decrire()
    data =  json.loads(agent.run(100))
    print(data)