
#Permet d'effacer ce qui est afficher à la console.
#Taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#By user: poke
from pydoc import cli
import tkinter as tk
import random
from tkinter import BOTH, BOTTOM, LEFT, RIGHT, TOP, messagebox
from turtle import left, right
from PIL import Image, ImageTk
from functools import partial
import random
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
class Card :
    suit_names = ["Coupe", "Epee", "Baton", "Denier"]
    rank_names = [None, "1", "2", "3", "4", "5", "6", "7",
                  "10", "11", "12"]
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        
    def __str__(self) :
        return '%s_%s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])


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
        for suit in range(4):
            for  rank in range(1, 11):
                card = Card (suit, rank)
                self.cards.append(card)
    def brasser (self):
        random.shuffle(self.cards)
   #Formate le paquet sous un string
    def __str__(self):
        str_deck = ""
        for i, card in enumerate(self.cards):
            str_deck += str(card) + " "
            if i%10 == 9:
                str_deck += " \n"
        return str_deck 

    def insert(self,i,carte):
        self.cards.insert(i,carte)

    def index(self,card):
        for i in range(self.leng_cards()):
            if card == self.cards[i]:
                return i
    def add_card(self, carte):
        self.cards.append(carte)

    def remove_card(self, carte):
        self.cards.remove(carte)
    def pop_card(self, i=-1):
        return self.cards.pop(i)
    def leng_cards(self):
        return len(self.cards)
    def carte(self,i):
        return self.cards[i]
    def sorted(self):
        p = Hand()
        for i in range(self.leng_cards()):
            petit = i
            for j in range(i+1,self.leng_cards()):
                if self.cards[j] > self.cards[petit]:
                    petit=j
                    self.cards[i],self.cards[petit]=self.cards[petit],self.cards[i]
        self.move_cards(p,self.leng_cards())
        return p
    def move_one_card(self, carte,autre):
            autre.add_card(carte)
            self.remove_card(carte)

    def move_cards(self, autre, num=1):
      while num > 0:
            autre.add_card(self.pop_card())
            num -= 1

    def move_cards_no_dbl(self, autre, num=1):
        avant = Card()
        while num > 0:
            current = self.pop_card()
            if avant != current:
                autre.add_card(current)
                avant = current
                num -= 1
class Hand(Paquet):
   
    def __init__(self, label=" "):
        self.cards = []
        self.points = 0
        self.gain_cards=[]
        self.label = label
        #super()._init__()
   #Formate le paquet sous un string
    def __str__(self):
        str_deck = ""
        for i, card in enumerate(self.cards):
            str_deck += str(card) + " "
            if i%10 == 9:
                str_deck += " \n"
        return str_deck  
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
def jeu():
    # declaration
    #p_joeur,p_ordi,dernier = joeur.points,ordi.points,""



    def affichage(paquet=Paquet(),joeur=Hand(),ordi=Hand(),table=Hand(),leng=0,mssg=""):
        cls()

        if mssg == "" and paquet.leng_cards() !=0:

            if leng==2:
                choix_joeur = f"|choix 1 = {joeur.cards[0]}  choix 2 = {joeur.cards[1]}|"
            elif leng ==3:
                choix_joeur  = f"|choix 1 = {joeur.cards[0]}  choix 2 = {joeur.cards[1]}  choix 3 = {joeur.cards[2]}|"   
            elif leng==1:
                choix_joeur = f"|choix 1 = {joeur.cards[0]}|"
            else:
                choix_joeur = ""
            win = tk.Toplevel(jeu)
            win.geometry("1000x800")
            win["bg"]= "SkyBlue2"
            win["relief"] = "raised"
            
            frame0=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
            frame0.pack(side=BOTTOM)
            frame_joeur=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
            frame_joeur.pack(side=BOTTOM)
            frame_table=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
            frame_table.pack(side=TOP)        
            btn1 = tk.Button(frame0,text="choix1",bg="SkyBlue2",command=clique_choix1)
            btn1.grid(row=0,column=0)
            btn2 = tk.Button(frame0,text="choix2",bg="SkyBlue2",command=clique_choix2)
            btn2.grid(row=0,column=1)
            btn3 = tk.Button(frame0,text="choix3",bg="SkyBlue2",command=clique_choix3)
            btn3.grid(row=0,column=2)
            btn_quit= tk.Button(frame0, text="Quit", command=win.destroy,bg="SkyBlue2")
            btn_quit.grid(row=1,column=0)
            frame3=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
            frame3.pack(side=TOP)        
            frame4=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
            frame4.pack(side=BOTTOM)        
            frame5=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
            frame5.pack(side=BOTTOM)
            points_ordi = ordi.points
            points_joeur = joeur.points
            lbl_table=tk.Label(frame3,font=("courier",30),text="cartes de la table ",bg="SkyBlue2").pack()
            lbl_points=tk.Label(frame4,font=("courier",20),text=f"Ordi points : {points_ordi}           vos points : {points_joeur}").pack()
            lbl_joeur=tk.Label(frame5,font=("courier",30),text=f"vos cartes ",bg="SkyBlue2")
            lbl_joeur.grid(row=0,column=1)
        else: 
                print(f"""
                ***************************************************************************************************
                            le resultat du jeu        {mssg}
                point joeur = {joeur.points}     point ordi = {ordi.points}
                ****************************************************************************************************
            """)
    def distribuer(paquet,table,joeur,ordi):
    
   
        if paquet.leng_cards() !=0:

            if paquet.leng_cards()==40:
                paquet.move_cards_no_dbl(table,4)

            paquet.move_cards(joeur,3)
            paquet.move_cards(ordi,3)
            joeur.pointage_randa_tringa(ordi)
        

    def sequence(card,table):
            p,l=Hand(),Hand()

            if card in table.cards:

                table=table.sorted()

                #p.add_card(card)
                current = card.rank
                for carte in table.cards:
                    if carte > card or carte == card:
                        suivant = current+1
                        
                        if carte.rank==7:
                            dif = 3
                        else:
                            dif = 1

                        if suivant-carte.rank == dif:
                            table.move_one_card(carte,p)
                            current = suivant
                        else:
                            break
            return p,table 


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

    def parti(ordi,joeur,table):
        paquet =Paquet()
        paquet.brasser()


        if paquet.leng_cards() != 0:
#            p_joeur,p_ordi,dernier = joeur.points,ordi.points,""
#            pj,po,p_joeur,p_ordi,dernier =0,0, joeur.points,ordi.points,""

            cond1 = False
            mssg =""
            while (not cond1):
                if paquet.leng_cards()== 0:
                    cond1 = True 
                else:
                    distribuer(paquet,table,joeur,ordi)
                    n_car_j, n_car_o = 0,0
                    while ordi.leng_cards() !=0:
                        affichage(paquet,joeur,ordi,table,joeur.leng_cards())
                        if joeur.points >= 41 or ordi.points >= 41:
                            return joeur.points, ordi.points
                        else:

                            cond = False
                            while (not cond):
                                

                                choix= input(" valider votre choix  :")

                                if choix == "1":
                                    n= joeur.cards[0]
                                    cond = True
                                elif choix == "2":
                                    n= joeur.cards[1]
                                    cond = True
                                elif choix == "3":
                                    n= joeur.cards[2]
                                    cond = True
                                elif choix == "":
                                    print("choix est vide")
                                else:
                                    print("la carte n'exixste pas ")

                            #affichage()
                                if choix == "1" or choix == "2" or choix == "3":
                                    dernier,table = tour(n,table,joeur)
                                    dernier,table = tour_ordi(ordi,table)  


            if joeur.points < 41 and  ordi.points < 41:       
                # donner les cartes de la table au gagnant a la fin
                if dernier == "j":
                    n_car_j = joeur.leng_gain() +  table.leng_cards()
                if dernier == "o":
                    n_car_o = ordi.leng_gain() +  table.leng_cards()
                # compter les cartes recettes
                if n_car_j > 20:
                    joeur.points += (n_car_j-20)
                elif n_car_o > 20:
                    ordi.points += (n_car_o-20)

            return joeur.points, ordi.points

    fin =False
    while (not fin):
        print("1-parti sinple ")
        print("2-jeu complet ")
        print("3-Quiter ")
        choix = int(input("Entrez votre choix : "))


        if choix == 1:
                joeur = Hand("j")
                ordi = Hand("o")
                table = Hand("t")

                p_joeur,p_ordi=parti(ordi,joeur,table)

                if p_joeur > p_ordi:
                        mssg= (f"Bravo vous avez gagne   avec {p_joeur} points contre {p_ordi}")
                elif p_ordi > p_joeur:
                        mssg= (f"vous avez perdu   avec {p_joeur} points contre {p_ordi} ")
                else:
                        mssg= (f"egalite")
                affichage(mssg)
                
        if choix == 2:
            joeur = Hand("j")
            ordi = Hand("o")
            table = Hand("t")
            cond2 = False
            while(not cond2):
                p_joeur,p_ordi = parti(ordi,joeur,table)
                if p_joeur >= 41:
                    mssg= (f"Bravo vous avez gagne   avec {p_joeur} points contre {p_ordi}")
                    cond2 = True
                elif p_ordi >= 41:
                    mssg= (f"vous avez perdu   avec {p_joeur} de points contre {p_ordi} ")
                    cond2 = True
                else:
                    affichage(f"Le score est : vous = {p_joeur} et ordi {p_ordi}")
                    input(" cliquer pour continue")

            affichage(mssg)
        if choix == 3:
            fin = True


jeu()

"""
distribuer(paquet,table,joeur,ordi)
    #p_joeur+=p1
    #p_ordi +=p2
    print(paquet)
    print(joeur)
    print(ordi)
    print(table)
    #print(p_joeur)
    #print(p_ordi)
    print(joeur.points)
    print(ordi.points)
    print(joeur.liste_gain())
    #



#    global jouer, ordi, carte,table, r_joeur, r_ordi,p_joueur, p_ordi,dernier
#    jouer, ordi, carte,table, r_joeur, r_ordi=[],[],[],[],[],[]
#    carte= paquet.cards
#    joeur=o_joeur.cards
#    ordi =o_ordi.cards
#    table=o_table.cards
    


 

#
    
    
    print(paquet)
    #print(paquet)
    distribuer(paquet,table,joeur,ordi)
    p_joeur, p_ordi, dernier = joeur.points,ordi.points,""
    print(table)
    print(joeur.cards[0])
    print(ordi)
    print(p_joeur)
    print(p_ordi)
    affichage(p_joeur,p_ordi,paquet,joeur,ordi,table,3,"")
    print(joeur)
    #print(p_ordi)
    #table=table.sorted()
    dernier,table = tour(joeur.cards[0],p_joeur,table,joeur)
    print(joeur.liste_gain())
    print(table)
    print(joeur)
""" 
