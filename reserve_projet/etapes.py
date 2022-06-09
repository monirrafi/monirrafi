
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
    def __init__(self, rank=0,suit=""):
        self.suit = suit
        self.rank = rank

    def __str__(self) :
        return f"{self.rank}_{self.suit}"

        #return '%s_%s' % (Card.rank_names[self.rank],                             Card.suit_names[self.suit])
    def __repr__(self): 
        return str(self.rank) +"_"+ self.suit
        #return str(Card.rank_names[self.rank]) + "_" + Card.suit_names[self.suit] 
    def image(self):
        return str(self.rank) + self.suit

        #return Card.suit_names[self.suit] + Card.rank_names[self.rank] 

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
class Paquet:
    def __init__(self):
        self.cards = []
        suit_names = ["Coupe", "Epee", "Baton", "Denier"]
        rank_names = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        
        #Créé les 10 cartes de chaque suite en ordre
        for s in suit_names:
            for n in rank_names:
                self.cards.append(Card(n, s))
   #Formate le paquet sous un string
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

    def carte(self,i):
        return self.cards[i]
    
    def move_one_card(self, carte,autre):
            autre.add_card(carte)
            self.remove_card(carte)

    def move_cards(self, autre):
      i=0
      while i<3:
            autre.add_card(self.pop_card())
            i += 1

    def move_cards_no_dbl(self, autre):
        i=1
        autre.add_card(self.pop_card())
        while i<4:
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
   
    def __init__(self, label=" "):
        self.cards = []
        self.points = 0
        self.gain_cards=[]
        self.label = label
        #super().__init__(cards)
   #Formate le paquet sous un string
    def __str__(self):
        str_deck = ""
        for i, card in enumerate(self.cards):
            str_deck += str(card) + " "
            if i%10 == 9:
                str_deck += " \n"
        return str_deck  
    def trouve_index_rank(self,card):
        
        for carte in self.cards:
            if carte == card:
                return self.cards.index(carte)

        return None

    def sort_list(self):
        stdls = self.cards
        for i in range(len(stdls)):
            minval = i
            for j in range(i+1, len(stdls)):
                if stdls[minval].rank > stdls[j].rank:
                    minval = j
                    stdls[i], stdls[minval] = stdls[minval], stdls[i]
        
        return stdls
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
    def liste_gain(self):
        gain = ""
        for item in self.gain_cards:
            gain = item.__str__() + " " + gain 
        return gain

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

    def leng_gain(self):
        return len(self.gain_cards)
    def dic(self):
        dic = {}
        for i in range(self.leng_cards()):
            dic[self.cards[i]]=self.cards[i].rank
        return dic
#######################################################################################################
#
#   les fonctions
############################################################################################################
def jeu():

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
             
    def distribuer(paquet,table,joeur,ordi):
        paquet.brasser()
        if paquet.leng_cards() !=0:
            if paquet.leng_cards()==40:
                paquet.move_cards_no_dbl(table)

            paquet.move_cards(joeur)
            paquet.move_cards(ordi)
            #donner les points ronda et tiringa
            joeur.pointage_randa_tringa(ordi)

    def tour_ordi(ordi,table):
        dernier,res = "",""
        
        o =Hand()
        for co in ordi.cards:
            o,table = sequence(co,table)
            if o.leng_cards() != 0:
                #cas de essti
               
                for item in o.cards:
                    if item == o.cards[0] and o.label == "j":
                        ordi.points += 1

                    ordi.gain_cards.append(item)
                    #table.remove_(item)
                    #table.remove_card(item)
                ordi.gain_cards.append(co)
                ordi.remove_card(co)
                res = "o"
                dernier = "o"
                break
        if res == "":
            dernier = "o"
            table.add_card(ordi.cards[0])
            ordi.remove_card(ordi.cards[0])

        
        return dernier,table

    def tour(n,table,joeur):
        j=Hand()
        j,table=  sequence(n,table)
        if j.leng_cards() != 0:
            # cas de essti
            for item in j.cards:
                if item == j.cards[0] and j.label == "o":
                    joeur.points += 1
                joeur.gain_cards.append(item)
                #table.remove_card(item)
                #table.remove_card(item)
            joeur.gain_cards.append(n)
            dernier = "j"
        else:
            dernier = "o"
            table.add_card(n)
        joeur.remove_card(n)

        return dernier,table


    def sequence(card,table):
            p,table_sorted=Hand(),[]
            carte = Card()
            current = table.trouve_index_rank(card)
            if current != None:
                carte = table.cards[current]
                table_sorted = sorted(table.cards)
                current= table_sorted.index(carte)
                #table.move_one_card(carte,p)
                for i in range(current,len(table_sorted)-1):
                        suivant = current+1
                        if table_sorted[current].rank==7:
                            dif = 3
                        else:
                            dif = 1
                        a=table_sorted[current].rank 
                        b=table_sorted[suivant].rank    
                        if table_sorted[suivant].rank - table_sorted[current].rank == dif:
                            table.move_one_card(table_sorted[suivant],p)
                            current = suivant
                        else:
                            break
                table.move_one_card(carte,p)
                
            return p,table 

    def parti(ordi,joeur,table):
            paquet =Paquet()
#        if paquet.leng_cards() != 0:

            cond1 = False
            while (not cond1):
                if paquet.leng_cards()== 0:
                        return joeur.points, ordi.points
                else:
                    distribuer(paquet,table,joeur,ordi)
                    leng_ordi = ordi.leng_cards()
                    n_car_j, n_car_o = 0,0
                    #cond = False
                    while joeur.leng_cards() !=0:
                        
                        if joeur.points >= 41 or ordi.points >= 41:
                            return joeur.points, ordi.points
                        else:
                                    if paquet.leng_cards()== 0:
                                          cond1=True  
                                    affichage("",paquet.leng_cards(),joeur,ordi,table,"",joeur.leng_cards())

                                    choix= input(" valider votre choix  :")
                                    
                                    if choix == "1":
                                        n= joeur.cards[0]
                                        cond = True
                                    elif choix == "2" and joeur.leng_cards() >= 2:
                                            n= joeur.cards[1]
                                            cond = True
                                    elif choix == "3" and joeur.leng_cards() >= 3:
                                            n= joeur.cards[2]
                                            cond = True
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
                    for carte in table.cards:
                        joeur.gain_cards.append(carte)
                        table.remove_card(carte)

                    n_car_j = joeur.leng_gain() 
                    dernier = f"les {table.leng_cards()} cartes de la table pour vous "
                if dernier == "o":
                    for carte in table.cards:
                        ordi.gain_cards.append(carte)
                        table.remove_card(carte)
                    n_car_o = ordi.leng_gain() 
                    dernier = f"les  {table.leng_cards()} cartes de la table pour l'ordi "
                # compter les cartes recettes
                n_car_j= joeur.leng_gain()
                n_car_o= ordi.leng_gain()
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
    fin =False
    while (not fin):

        print("1-parti sinple ")
        print("2-jeu complet ")
        print("3-Quiter ")
        
        choix = input("Entrez votre choix du jeu : ")


        if choix == "1":
                joeur = Hand("j")
                ordi = Hand("o")
                table = Hand("t")

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
                joeur = Hand("j")
                ordi = Hand("o")
                table = Hand("t")

                r_pjoeur,r_pordi=parti(ordi,joeur,table)
                p_joeur += r_pjoeur
                p_ordi += r_pordi
                if p_joeur >= 11:
                        mssg= (f"Bravo vous avez gagne   avec {p_joeur} points contre {p_ordi}")
                        cond2=True
                elif p_ordi >=11:
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

"""
    paquet = Paquet()
    table=Hand()
    joeur=Hand("j")
    ordi=Hand("o")
    p=Hand()
    paquet.brasser()
    #print(paquet)
    distribuer(paquet,table,joeur,ordi)
    p_joeur, p_ordi, dernier = joeur.points,ordi.points,""
    #print(joeur.cards[0])
    print("table")
    print(table)
    print("joeur")
    print(joeur)
    #print(joeur.cards[0].rank)
    print("ordi")
    print(ordi)
    #affichage(paquet,joeur,ordi,table,3,"")
    #table=table.sorted()
    print("=============")
    #print(table)

    dernier,table = tour(joeur.cards[0],table,joeur)
    print(dernier)
    dernier,table = tour_ordi(ordi,table)

    print(dernier)
    #print(sorted(table.cards))
    #print(sort_l(table))
    #print(table.trouve_rank(joeur.cards[0]))
    #table.sorted()
    print("=============")
    #p,table=sequence(joeur.cards[0],table)

    print("table")
    print(table)
    #print("p")
    #print(p)
    print("joeur")
    print(joeur)
    print("ordi")
    print(ordi)
    print(joeur.liste_gain())
    print(ordi.liste_gain())
    print(p_joeur)
    print(p_ordi)
    #l=[2,5,18,1,3,12,10,5,46,4]
    #print(sorted(l))


#    global jouer, ordi, carte,table, r_joeur, r_ordi,p_joueur, p_ordi,dernier
#    jouer, ordi, carte,table, r_joeur, r_ordi=[],[],[],[],[],[]
#    carte= paquet.cards
#    joeur=o_joeur.cards
#    ordi =o_ordi.cards
#    table=o_table.cards
"""    


 


    
    
 
