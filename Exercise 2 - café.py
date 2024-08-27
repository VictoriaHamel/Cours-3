choix = [
# (nom , distance en km , qualite sur 10)
( " Starbucks" , 1.2 , 8) , #7.8 0.15
( " Cafe local" , 0.5 , 7) , #6.5 0.071
( " Pete’s Coffee" , 1.8 , 9) , #7.2 0,2
( " Dunkin’ Donuts" , 0.8 , 6),# 5.2 0,13
    ( 'Tim', 0.1, 1) # 0.9 0.1
]

def meilleur_cafe(choix):
    meilleur = None
    indice = 1
    for cafe in choix:
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