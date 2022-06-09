
#Permet d'effacer ce qui est afficher à la console.
#Taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#By user: poke
import random
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
##########################################################################################
#  les classes
###########################################################################################
class Card :
    def __init__(self, rank=0,suit="",label=""):
        self.suit = suit
        self.rank = rank
        self.label=label

    # pour affichage des cartes sous forme Numero_Suite(7_Coupe)
    def __str__(self) :
        return f"{self.rank}_{self.suit}"

    # 3 methodes pour la comparaison entre les cartes 
    def __lt__(self, autre):
        t1 = self.rank
        t2 = autre.rank
        return t1 < t2
    def __gt__(self, autre):
        t1 = self.rank
        t2 = autre.rank
        return t1 > t2
    def __eq__(self, autre):
        t1 = self.rank
        t2 = autre.rank
        return t1 == t2

    # utiliser dans la lecture des fichiers image
    def image(self):
        return str(self.rank) + self.suit
class Paquet:
    def __init__(self):
        self.cards = []

        suit_names = ["Coupe", "Epee", "Baton", "Denier"]
        rank_names = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        
        #Créé les 10 cartes de chaque suite en ordre
        for s in suit_names:
            for n in rank_names:
                self.cards.append(Card(n, s))

   # Formate le paquet sous un string pour affichage
    def __str__(self):
        str_deck = ""
        for i, card in enumerate(self.cards):
            str_deck += str(card) + " "
            if i%10 == 9:
                str_deck += " \n"
        return str_deck 
    
    def brasser (self):
        random.shuffle(self.cards)


    def add_card(self, carte):
        self.cards.append(carte)
        
    def remove_card(self, carte):
        self.cards.remove(carte)

    def pop_card(self, i=0):
        if len(self.cards) !=0:
            return self.cards.pop(i)

    def leng_cards(self):
        return len(self.cards)
    # retourne une carte a un index precise
    def carte(self,i):
        return self.cards[i]
    
    def move_one_card(self, carte,autre):
            autre.add_card(carte)
            self.remove_card(carte)

    def move_cards(self, autre,label,n=1):
      i=0
      while i<n:
            carte=self.pop_card()
            carte.label=label
            autre.add_card(carte)
            i += 1

    def move_cards_no_dbl(self, autre,n=0):
        i=1
        autre.add_card(self.pop_card())
        while i<n:
            trouve=False
            current = self.pop_card()
            for c in autre.cards:
                if c == current:
                    self.add_card(current)
                    trouve = True
                    break
            if trouve==False:
                autre.add_card(current)
                i += 1
            

class Hand(Paquet):
   
    def __init__(self):
        self.cards = []
        self.points = 0
        self.gain_cards=[]

    def trouve_index_rank(self,card):
        for carte in self.cards:
            if carte == card:
                return self.cards.index(carte)
        return None

    # fonction retourne la liste des cartes gagnées                  
    def liste_gain(self):
        gain = ""
        for item in self.gain_cards:
            gain = item.__str__() + " " + gain 
        return gain
    # fonction retourne le nombre des cartes gagnées
    def leng_gain(self):
        return len(self.gain_cards)

    # fonction verifier les Ronda et les tringas
    def verification(self):
        cpt = 0
        n= 0
        if self.cards[0] == self.cards[1] and self.cards[0] == self.cards[2]:
                cpt=3
                n=self.cards[0].rank
        if self.cards[0] == self.cards[1] or self.cards[0] == self.cards[2] or self.cards[1] == self.cards[2]:
                cpt=2
                n=self.cards[0].rank
        return cpt,n 

    # donne les points de ronda ou tringa pour chaque equipe
    def pointage_randa_tringa(self,autre):
        c1,n1 = self.verification() 
        c2,n2 = autre.verification() 
        if c1==2 and c2==0:
            self.points += 1
        elif c1==0 and c2==2:
            autre.points += 1
        elif c1==c2==2:
            if n1 > n2:
                self.points += 2
            elif n2 > n1:
                autre.points += 2
            else:
                self.points += 1
                autre.points += 1
        elif c1==0 and c2==3:
                autre.points += 5
        elif c1==3 and c2==0:
                self.points += 5
        elif c1==2 and c2==3:
                autre.points += 6
        elif c1==3 and c2==2:
                self.points += 6
        elif c1==c2==3:
            if n1 > n2:
                self.points += 10
            elif n2 > n1:
                autre.points += 10
            else:
                self.points += 5
                autre.points += 5
        return self.points,autre.points     

#######################################################################################################
#
#   les fonctions
############################################################################################################
def jeu():
    # fonction pour affiche le paneau du jeu
    def affichage(mssg="",lpaquet=0,joeur=Hand(),ordi=Hand(),table=Hand(),dernier ="",leng=0):
        cls()

        if mssg != "":
               print(f"""
                ***************************************************************************************************
                                    {mssg}

                ****************************************************************************************************
            """)
 
        else: 
            if leng==2:
                choix_joeur  = f"""
                choix 1 =   {joeur.cards[0]}  
                choix 2 =   {joeur.cards[1]}"""   
            elif leng ==3:
                choix_joeur  = f"""
                choix 1 =   {joeur.cards[0]}  
                choix 2 =   {joeur.cards[1]}  
                choix 3 =   {joeur.cards[2]}"""   
            elif leng==1:
                choix_joeur = f"""
                choix 1 =   {joeur.cards[0]}"""
            else:
                choix_joeur = ""

            print(f"""
            ==================================================================================================
            la table             |{table}|               
            {dernier}                
            les cartes de l'ordi |{ordi}|
            ==================================================================================================                                                                   
                                        {choix_joeur}                                    
            ===================================================================================================    
            carte jouer = {joeur.leng_gain()}                                 carte ordi = {ordi.leng_gain()} 

            le nombres des cartes restes à distribuer  = {lpaquet}

            les points de la partie :      vous = {joeur.points}   l'ordi = {ordi.points}
            ====================================================================================================
            """)
    # fonction de distribution des cartes entre paquet et les hands         
    def distribuer(paquet,table,joeur,ordi):
        paquet.brasser()
        if paquet.leng_cards() !=0:
            if paquet.leng_cards()==40:
                paquet.move_cards_no_dbl(table,4)

            paquet.move_cards(joeur,"j",3)
            paquet.move_cards(ordi,"o",3)
            #donner les points ronda et tiringa
            joeur.pointage_randa_tringa(ordi)

    # Fonction sequence (card, table) vérifier l’existence Rank d’une carte dans la table 
    # s’il existe il retourne toutes les cartes ayant les numéros suivants 
    # dans un objet hand et le reste de la table dans une autre liste 
    def sequence(card,table):
            p,table_sorted=Hand(),[]
            carte = Card()
            current = table.trouve_index_rank(card)
            if current != None:
                # sortir la carte semblable de la table
                carte = table.cards[current]
                # ordonner la table
                table_sorted = sorted(table.cards)
                current= table_sorted.index(carte)
                for i in range(current,len(table_sorted)-1):
                        suivant = current+1
                        if table_sorted[current].rank==7:
                            dif = 3
                        else:
                            dif = 1
                        if table_sorted[suivant].rank - table_sorted[current].rank == dif:
                            table.move_one_card(table_sorted[suivant],p)
                            current = suivant
                        else:
                            break
                table.move_one_card(carte,p)
            return p,table 
    
    # Fonction tour_ordi (ordi, table) appelée quand le tour de l’ordi arrive
    # Fonction tour (carte, table) reçoit une carte et appelée quand le tour du joueur arrive

    def tour_ordi(ordi,table):
        dernier= ""
        o =Hand()
        for co in ordi.cards:
            o,table = sequence(co,table)
            if o.leng_cards() != 0:
                #cas de missa
                if table.leng_cards() ==0:
                    ordi.points+=1
                # cas de essti
                lb=o.cards[-1].label
                l=o.cards
                if o.cards[-1].label=="j":
                    ordi.points += 1
                for item in o.cards:

                    ordi.gain_cards.append(item)
                ordi.gain_cards.append(co)
                ordi.remove_card(co)
                dernier = "o"
                break
        if dernier == "":
            dernier = "j"
            ordi.move_one_card(ordi.cards[0],table)
        return dernier,table

    def tour(n,table,joeur):
        j=Hand()
        j,table=  sequence(n,table)
        
        if j.leng_cards() != 0:
            # cas de missa
            if table.leng_cards() ==0:
                ordi.points+=1
            # cas de essti
            lb=j.cards[-1].label
            l=j.cards
            if j.cards[-1].label == "o":
                joeur.points += 1
            for item in j.cards:
                joeur.gain_cards.append(item)
                #table.remove_card(item)
                #table.remove_card(item)
            joeur.gain_cards.append(n)
            dernier = "j"
        else:
            dernier = "o"
            table.add_card(n)
            print(table.cards[-1])
            print(table.cards[-1].label)
        joeur.remove_card(n)

        return dernier,table
# Dans cette fonction le programme déclenche une grande boucle :
# On vérifier si la liste du paquet est vide sinon on entre dans une autre boucle en vérifiant 
# si toutes les cartes du joueur et ordi sont jouées sinon : 
# qui affiche avec Affichage ()
#   •	Les cartes de la table, 
#   •	Les cartes d’ordi (normalement ils faut qu’ils soient cachés mais seulement pour la démo) 
#   •	Les 3 cartes du joueur chacune a cote d’un choix.
# Demande au joueur de donner son choix on appelle les fonctions tour () et tour_ordi () qui vont faire la vérification sur les cartes de la table pour ramasser les mêmes cartes et leur suivies, les missa et les essti.
# Après le sorite de cette boucle on vérifier les points si quelqu’un à dépasser 41 points le jeu est terminer ou toutes les cartes du joueur et ordi sont jouées sinon on fait une autre distribution et appelle aux fonctions tour () et tour_ordi () une autre fois.
    def parti(ordi,joeur,table):
            paquet =Paquet()
            dernier=""
#        if paquet.leng_cards() != 0:

            cond1 = False
            while (not cond1):
                if paquet.leng_cards()== 0:
                        return 
                else:
                    distribuer(paquet,table,joeur,ordi)
                    #leng_ordi = ordi.leng_cards()
                    n_car_j, n_car_o = 0,0
                    #cond = False
                    while joeur.leng_cards() !=0:
                        
                        if joeur.points >= 41 or ordi.points >= 41:
                            return
                        else:
                                    if paquet.leng_cards()== 0:
                                          cond1=True  
                                    affichage("",paquet.leng_cards(),joeur,ordi,table,"",joeur.leng_cards())

                                    choix= input(" valider votre choix  :")
                                    
                                    if choix == "1":
                                        n= joeur.cards[0]
                                        #cond = True
                                    elif choix == "2" and joeur.leng_cards() >= 2:
                                            n= joeur.cards[1]
                                            #cond = True
                                    elif choix == "3" and joeur.leng_cards() >= 3:
                                            n= joeur.cards[2]
                                            #cond = True
                                    elif choix == "":
                                        print("choix est vide")
                                    else:
                                        print("la carte n'exixste pas ")

                                    if choix == "1" or (choix == "2" and joeur.leng_cards() >= 2) or (choix == "3" and joeur.leng_cards() >= 3):
                                        dernier,table = tour(n,table,joeur)
                                        dernier,table = tour_ordi(ordi,table)  
                
            n_car_j= joeur.leng_gain()
            n_car_o= ordi.leng_gain()
            if joeur.points < 41 and  ordi.points < 41:       
                # donner les cartes de la table au gagnant a la fin
                if dernier == "j":
                    n_car_j += table.leng_cards() 
                    dernier = f"le(s) {table.leng_cards()} carte(s) de la table pour vous "
                if dernier == "o":
                    n_car_o += table.leng_cards()
                    dernier = f"les  {table.leng_cards()} cartes de la table pour l'ordi "
                # compter les cartes recettes
                if n_car_j > 20:
                    joeur.points += (n_car_j-20)
                elif n_car_o > 20:
                    ordi.points += (n_car_o-20)


                affichage("",paquet.leng_cards(),joeur,ordi,table,dernier,joeur.leng_cards())
                wait = input("PRESS ENTER TO CONTINUE.")


            return joeur.points, ordi.points

########################################################################################################

#   Programme
##########################################################################################################

# le menu principal
    fin =False
    while (not fin):

        print("1-partie simple ")
        print("2-jeu complet ")
        print("3-Quiter ")
        
        choix = input("Entrez votre choix du jeu : ")


        if choix == "1":
                joeur = Hand()
                ordi = Hand()
                table = Hand()

                p_joeur,p_ordi=parti(ordi,joeur,table)

                if p_joeur > p_ordi:
                        mssg= (f"Bravo vous avez gagne   avec {p_joeur} points contre {p_ordi}")
                elif p_ordi > p_joeur:
                        mssg= (f"vous avez perdu   avec {p_joeur} points contre {p_ordi} ")
                else:
                        mssg= (f"egalite est resultat finale")
                affichage(mssg)
                
        elif choix == "2":
            r_pjoeur,r_pordi =0,0
            p_joeur,p_ordi=0,0
            cond2 = False
            while(not cond2):
                joeur = Hand()
                ordi = Hand()
                table = Hand()

                r_pjoeur,r_pordi=parti(ordi,joeur,table)
                p_joeur += r_pjoeur
                p_ordi += r_pordi
                if p_joeur >= 41:
                        mssg= (f"Bravo vous avez gagne   avec {p_joeur} points contre {p_ordi}")
                        cond2=True
                elif p_ordi >=41:
                        mssg= (f"vous avez perdu   avec {p_joeur} points contre {p_ordi} ")
                        cond2=True
                else:
                    affichage(f"le score apres cette partie est  vos {p_joeur} points contre {p_ordi} de l'ordi")
                    wait = input("PRESS ENTER TO CONTINUE LA PROCHAINE PARTIE")

            affichage(mssg)

        elif choix == "3":
            fin = True
        else:
            print("Votre choix n'est pas valide  ")


jeu()
