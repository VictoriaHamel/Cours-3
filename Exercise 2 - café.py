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

# print(liste_cafés[0] == liste_cafés[1])    return difference



cafes = [('CafeA', 10, 1), ('CafeB', 10, 10), ('CafeC', 8, 1), ('CafeD', 9, 2), ('CafeE', 11, 3),
    ('CafeZero',0,10), ('CafeTresProche',0.1,11), ('CafeTresLoin', 100, 110000)]



class Cafe:
    def __init__(self, nom, distance, qualite):
        self.nom = nom
        self.distance = distance
        self.qualite = qualite
        if distance == 0 or distance < 1:
            distance = 0.1
        if distance > 15:
            distance = 1
            qualite = 0

        self.score = qualite / distance

    def __str__(self):
        print("Function __str")
        return f"{self.nom} est à {self.distance} km et a une qualité de {self.qualite}."

    def __repr__(self):
        print("Function __rep")
        return f"{self.nom}"


    def __eq__(self, other):
        return self.score - other.score



liste_cafes = []
for cafe in cafes:
    liste_cafes.append(Cafe(cafe[0], cafe[1], cafe[2]))

liste_cafes.sort(key=lambda x: x.score, reverse=True)

print(liste_cafes[0])







