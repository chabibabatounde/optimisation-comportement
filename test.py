# coding: utf-8
from Algo_Genetique.AlgoGenetique import * 
from Immunitaire.Immunitaire import * 
from Modules.Probleme import * 
from Modules.Graphique import * 

#Probleme d'origine
solutionDeBase = Solution([1.0,0.9,0.2], [2.0,1.0,0.1], [2.5,3.8,1.1], [1.2,2.2,0.455], [0.1,0.6,0.35],20.0, 80.0)
figure = Graphique()
figure.single(solutionDeBase, "Comportement connu_im")
#Création d'une instance de probleme d'optimisation
probleme = Probleme("dataset.json")

#Création d'une instance de l'algo d'optimisation
#algorithme = AlgoGenetique(probleme= probleme, maxIterration=1000, taillePopulation=1000, nombreCroisement=50)
algorithme = Immunitaire(probleme= probleme, maxIterration=100,  proportion=60, nbAnticorps=500)

#Lancement du calcul
#resultats = algorithme.optimiser()

#resultats =  Solution([0.016581757920766105,0.027074122562112946,0.15180168201147914],[2.9015984944512487,1.6028443503479588,0.019841082718687675],[3.7158569315330805,5.616026964093096,1.2317909586915132],[1.7407482638076077,3.0545963524752184,0.5689979024119851],[0.0972053565435993,0.6147947084854799,0.3203775018194843],9.844377667951935,65.69756582064186)
resultats =  Solution([2.158203345970147, -1.3168070301486035, -1.6020522293955706], [6.677434786421506, -0.7751844136172004, 3.514145496385355], [2.260689201730907, 6.1589894687299465, 3.1124339929892253], [-1.8821810936239423, 3.826055512128177, -0.07201091901756107], [5.140209030408349, -1.2159158081201715, -0.05967644934728611], 6.11226468202629, 25.1358806908299)
#Affichage du Résultat
figure.single(resultats, "Comportement obtenu_im")
figure.multiple(solutionDeBase, "Comportement connu_im", resultats,  "Comportement obtenu_im")
resultats.decrire()
