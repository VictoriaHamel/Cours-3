choix = [
# (nom , distance en km , qualite sur 10)
( " Starbucks" , 1.2 , 8) , #7.8 0.15
( " Cafe local" , 0.5 , 7) , #6.5 0.071
( " Pete’s Coffee" , 1.8 , 9) , #7.2 0,2
( " Dunkin’ Donuts" , 0.8 , 6),# 5.2 0,13
    ( 'Tim', 0, 0) # 0.9 0.1
]

def meilleur_cafe(choix):
    meilleur = None
    indice = 10
    for cafe in choix:
        if not cafe[2] == 0:
            ratio = cafe[1] / cafe[2]
            if ratio < indice:
                indice = ratio
                meilleur = cafe
    return meilleur

        #for distance in cafe:
        #if cafe[1] < distance_max:
            #distance_max = cafe[1]
           # print(distance_max)


resultat = meilleur_cafe(choix)
print(f" Le meilleur cafe est { resultat[0] }. " )

# solution OO

class Café:
    def __init__(self, nom, disance, qualité):
        self.nom = nom
        self.disance = disance
        self.qualité = qualité
        if disance == 0 or disance < 1:
            disance = 0.00001
        if disance > 15:
            disance = 1
            qualité = 0
        self.score = qualité/disance

    def __str__(self):
        return f"{self.nom} est a {self.disance} km et a une qualité de {self.qualité}."

    def __repr__(self):
        print("Function __rep")
        return f"{self.nom}"

    def __eq__(self, other):
        return self.score - other.score

    #def calculer_score(self):


liste_cafés = []
for cafe in choix:
    liste_cafés.append(Café(cafe[0], cafe[1], cafe[2]))

liste_cafés.sort(key=lambda x: x.score, reverse=True)
print(liste_cafés[0])
# print(liste_cafés[0] == liste_cafés[1])    return difference