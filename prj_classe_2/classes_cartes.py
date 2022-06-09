# https://allen-downey.developpez.com/livres/python/pensez-python/?page=heritage

from multiprocessing import Value
import random
from socket import create_server
class Carte:
    def __init__(self, num, suite):
        self.num = num 
        self.suite = suite

    def __str__(self):

        #Formatte le chiffre/la lettre de la carte pour 
        #qu'elle prenne toujours 3 espaces et ajoutes la suite
        return f"{self.num:3}{self.suite}"


class Paquet:
    def __init__(self):
        noms_couleurs = ['Coupée', 'Epee', 'Baton', 'Denier']
        noms_valeurs = ['1', '2', '3', '4', '5', '6', '7', 
              '10', '11', '12']

        self.dic={}
        self.cartes=[]
        self.valeur=[]
        for couleur in noms_couleurs:
            for valeur in noms_valeurs:
                carte = Carte(valeur, couleur)
                a= carte.num
                b=carte.suite
                s=f"{a:3}{b}"
                self.dic[s]=int(a)
        self.cartes = list(self.dic.keys())
        self.valeur = list(self.dic.values())
    def trouve_valeur(self,i):
        return(self.cartes[i])
        
    
    def comparer_deux(self,un,autre):
        cond = "none"
        for carte_un in un.cartes:
            for carte in autre.cartes:
                a= un.valeur[un.cartes.index(carte_un)]
                b=autre.valeur[autre.cartes.index(carte)]
                if un.valeur[un.cartes.index(carte_un)]== autre.valeur[autre.cartes.index(carte)]:
                    cond = carte
                    break
    
        return cond

    

    def len_paquet(self):
        return len(self.cartes)

    def pop_carte(self):
        carte = self.cartes.pop(0)
        valeur = self.valeur.pop(0)
        return carte,valeur
 
    def ajouter_carte(self, carte,valeur):
        self.cartes.append(carte)
        self.valeur.append(valeur)

    def deplacer_cartes(self, hand, nombre):
        for i in range(nombre):
            carte,valeur = self.pop_carte()
            hand.ajouter_carte(carte,valeur)  
    def battre(self):
        random.shuffle(self.cartes)   
    def __str__(self):
        res = []
        for carte in self.cartes:
            res.append("[" + str(carte) + "]")
        return " ".join(res) 
class SousPaquet(Paquet):
    def __init__(self):
        self.dic ={}
        self.cartes = []
        self.valeur=[]
        

if __name__ == "__main__":
    paquet = Paquet()
    joeur = SousPaquet()
    table = SousPaquet()
    #print(paquet)

    #paquet.battre()
    #print(paquet)
    paquet.deplacer_cartes(joeur,3)
    #paquet.deplacer_cartes(table,4)

    print(joeur)
    #print(table)

    print(joeur.trouve_valeur(1))
    