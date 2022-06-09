
#Permet d'effacer ce qui est afficher à la console.
#Taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#By user: poke
from cProfile import label
from logging import root
import random
import os
from re import S
from telnetlib import SE
from textwrap import fill
import tkinter as tk
import random
from tkinter import BOTH, BOTTOM, CENTER, LEFT, RIGHT, SW, TOP, messagebox
from traceback import clear_frames
from turtle import left, right
from PIL import Image, ImageTk
from functools import partial
import tkinter.scrolledtext as st
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
    def __str__(self) :
        return f"{self.rank}_{self.suit}"

    def __repr__(self): 
        return str(self.rank) +"_"+ self.suit
        #return str(Card.rank_names[self.rank]) + "_" + Card.suit_names[self.suit] 
    def image(self):
        return self.suit + str(self.rank)

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

        suit_names = ["coupe", "épée", "baton", "denier"]
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
        #carte.label = label
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
#######################################################################################################
#
#   les fonctions
############################################################################################################
             
def distribuer(paquet,table,joeur,ordi):
    paquet.brasser()
    if paquet.leng_cards() !=0:
        if paquet.leng_cards()==40:
            paquet.move_cards_no_dbl(table,4)

        paquet.move_cards(joeur,"j",3)
        paquet.move_cards(ordi,"o",3)
        #donner les points ronda et tiringa
        joeur.pointage_randa_tringa(ordi)

    return table,joeur,ordi
def sequence(card,table):
        p,table_sorted=Hand(),[]
        carte = Card()
        # verifier l'existance de la carte dans la table 
        # retourne son index
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
            if o.cards[-1].label=="j":
                ordi.points += 1
            for item in o.cards:

                ordi.gain_cards.append(item)
                #table.remove_(item)
                #table.remove_card(item)
            ordi.gain_cards.append(co)
            ordi.remove_card(co)
            dernier = "o"
            break
    if dernier == "":
        dernier = "j"
        ordi.move_one_card(ordi.cards[0],table)
#            table.add_card(ordi.cards[0])
#            ordi.remove_card(ordi.cards[0])

    
    return dernier,table

def tour(n,table,joeur):
    j=Hand()
    j,table=  sequence(n,table)
    
    if j.leng_cards() != 0:
        # cas de missa
        if table.leng_cards() ==0:
            joeur.points+=1
        # cas de essti
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
    joeur.remove_card(n)

    return dernier,table
#=================================================================================================
# Fonctions ajoutées pour le graphique
#==================================================================================================

# fonction reçoit nom de la carte cherche et retourne son image
def load_image(card):
    card_name = "C:\\Users\\user\\Documents\\GitHub\\Ronda\\" 
    card_name = card_name + card.image() + ".png"
    return ImageTk.PhotoImage(Image.open(card_name))

# fonction retourne une liste des images
def convert_image(l):
    l_image=[]
    for carte in l:
        l_image.append(load_image(carte))
    return l_image

# fonction creer une etiquette image et la posiitonne dans une frame 
# pour les listes des images joueur, table et ordi
def make_label(master, ima,i,j):
    label= tk.Label(master,image=ima,relief=tk.RAISED,borderwidth=1)
    label.image=ima
    label.grid(row=i,column=j,padx=5,pady=5)
    return label

# fonction reçoit une liste des images et les afficher dans des lignes de 16
def display(master,liste):
    if len(liste)>16:
        for j in range(len(liste)//2+1):
                label=make_label(master,liste[j],0,j)
        for j in range(len(liste)//2):
                label=make_label(master,liste[j+len(liste)//2+1],1,j)
    else:
        for j in range(len(liste)):
                label=make_label(master,liste[j],0,j)
########################################################################################################

#   Programme du graphique 
##########################################################################################################
class Affichage():
    def __init__(self,root,paquet=None,table=None,joeur=None,ordi=None):
        
        self.paquet = paquet
        self.ordi=ordi
        self.joeur=joeur
        self.carte1=self.joeur.cards[0]
        self.carte2=self.joeur.cards[1]
        self.carte3=self.joeur.cards[2]
        self.table=table
        self.table_image =convert_image(table.cards)
        self.dernier =""

        self.frame_table = tk.Frame(root,padx=5,pady=5,bg="Green")
        self.frame_ordi = tk.Frame(root,padx=5,pady=5,bg="Green")
        self.frame_joeur1 = tk.Frame(root,padx=40,pady=20,bg="Green")
        self.frame_joeur2 = tk.Frame(root,padx=40,pady=20,bg="Green")
        self.frame_joeur3 = tk.Frame(root,padx=40,pady=20,bg="Green")
        self.lbl_points = tk.Label(root)

        self.frame3=tk.Frame(root,padx=5,pady=5,bg="Green")
        self.frame4=tk.Frame(root,padx=5,pady=5,bg="Green")
        self.frame5=tk.Frame(root,padx=5,pady=5,bg="Green")
        self.frame6=tk.Frame(root,padx=5,pady=5,bg="Green")
        self.frame7=tk.Frame(root,padx=5,pady=5,bg="Green")
        self.frame8=tk.Frame(root,padx=5,pady=5,bg="Green")
        self.frame_joeur=tk.Frame(root,padx=5,pady=5,bg="Green")



    def initial(self,root,ordi,carte1,carte2,carte3):
        self.frame_principal = tk.Frame(root,bg="Green").pack(fill=tk.X,side=TOP)
        self.btn_quitter=tk.Button(self.frame_principal, text="Quit", command=jeu.destroy)
        self.btn_quitter.pack(side=BOTTOM,padx=10,pady=10)
        self.btn_simple = tk.Button(self.frame_principal, text="Jeu simple vainceur qui gagne une partie "
        ,command=partial(self.clear_frame_table,ordi,carte1,carte2,carte3))
        self.btn_simple.pack(side=TOP,padx=10,pady=10)
        self.btn_complet = tk.Button(self.frame_principal, text="Explication du Jeu")
        self.btn_complet.pack(side=TOP,padx=10,pady=10)

    def show(self,root):
        root["bg"]="Green"
        self.frame3.pack(side=TOP)        
        self.frame_table.pack(expand=True,side=TOP,fill=BOTH)        
        self.frame6.pack(side=TOP)
        self.frame7.pack(side=TOP)
        self.frame_ordi.pack(expand=True,side=TOP,fill=BOTH)        
        self.frame8.pack(side=TOP)
        self.frame5.pack(side=BOTTOM)
        self.frame4.pack(side=BOTTOM)        

        self.frame_joeur.pack(side=BOTTOM)
        self.frame_joeur1.pack(side=LEFT)
        self.frame_joeur2.pack(side=LEFT)
        self.frame_joeur3.pack(side=LEFT)
        lbl_table=tk.Label(self.frame3,font=("courier",10),text=f"cartes de la table     "
        ,bg="Green").pack(side=TOP)
        lbl_ordi=tk.Label(self.frame7,font=("courier",10),text=f"cartes de l'ordinateur     "
        ,bg="Green").pack(side=TOP)
        lbl_joeur=tk.Label(self.frame8,font=("courier",10),text=f"Vos cartes     "
        ,bg="Green").pack(side=TOP)
        display(self.frame_table,self.table_image)

    def change_show(self,root,ordi,carte1,carte2,carte3):
        root["bg"]="Green"
        self.ordi_image =convert_image(ordi.cards)
        self.image1=load_image(carte1)
        self.image2=load_image(carte2)
        self.image3=load_image(carte3)
        if paquet.leng_cards()==0:
            mssg=""
            if self.joeur.points > self.ordi.points:
                mssg = f" Bravo vous avez gagné {self.joeur.points} contre {self.ordi.points}"                            
            elif self.ordi.points > self.joeur.points:
                mssg = f" vous avez perdu {self.joeur.points} contre {self.ordi.points}" 
            else:
                mssg = f"Égalité {self.joeur.points} contre {self.ordi.points}"  
#            self.frame3.pack(side=TOP)        
#            self.frame4.pack(side=BOTTOM)        
#            self.frame5.pack(side=TOP)
#            self.frame6.pack(side=BOTTOM)
#            lbl_table=tk.Label(self.frame3,font=("courier",10),text=f"Sommaire de la partie    ",bg="Green").pack()
            self.lbl_points=tk.Label(self.frame4,font=("courier",10)
            ,text=f"Les points de la partie : Ordi {self.ordi.points}  Vous : {self.joeur.points}"
            ,bg="Green").pack()
            lbl_gain=tk.Label(self.frame5,font=("courier",20),text=mssg).pack()
            lbl_paquet=tk.Label(self.frame6,font=("courier",10)
            ,text=f"Les cartes restantes :    {self.paquet.leng_cards()}",bg="Green" ).pack()
        else:
#            self.frame3.pack(side=TOP)        
#            self.frame_table.pack(expand=True,side=TOP,fill=BOTH)        
#            self.frame6.pack(side=TOP)
#            self.frame7.pack(side=TOP)
#            self.frame_ordi.pack(expand=True,side=TOP,fill=BOTH)        
#            self.frame8.pack(side=TOP)
#            self.frame5.pack(side=BOTTOM)
#            self.frame4.pack(side=BOTTOM)        

#            self.frame_joeur.pack(side=BOTTOM)
#            self.frame_joeur1.pack(side=LEFT)
#            self.frame_joeur2.pack(side=LEFT)
#            self.frame_joeur3.pack(side=LEFT)
            btn1 = tk.Button(self.frame_joeur1,text="choix1",bg="Green",command=partial(self.clique_choix
            ,carte1,self.frame_joeur1))
            btn1.grid(row=0,column=1)
            btn2 = tk.Button(self.frame_joeur2,text="choix2",bg="Green",command=partial(self.clique_choix
            ,carte2,self.frame_joeur2))
            btn2.grid(row=0,column=1)
            btn3 = tk.Button(self.frame_joeur3,text="choix3",bg="Green",command=partial(self.clique_choix
            ,carte3,self.frame_joeur3))
            btn3.grid(row=0,column=1)
#            lbl_table=tk.Label(self.frame3,font=("courier",10),text=f"cartes de la table     "
#            ,bg="Green").pack(side=TOP)
#            lbl_ordi=tk.Label(self.frame7,font=("courier",10),text=f"cartes de l'ordinateur     "
#            ,bg="Green").pack(side=TOP)
#            lbl_joeur=tk.Label(self.frame8,font=("courier",10),text=f"Vos cartes     "
#            ,bg="Green").pack(side=TOP)
            lbl_points=tk.Label(self.frame4,font=("courier",10)
            ,text=f"Les points de la partie :   Ordi {self.ordi.points}           Vous : {self.joeur.points}").pack(side=LEFT)
            lbl_gain=tk.Label(self.frame5,font=("courier",10)
            ,text=f"Les cartes gagnées de la partie :   Ordi : {self.ordi.leng_gain()}  Vous : {self.joeur.leng_gain()}  ")
            lbl_gain.grid(row=0,column=1)
            lbl_paquet=tk.Label(self.frame6,font=("courier",10),text=f"Les cartes restantes :           paquet : {self.paquet.leng_cards()}" ).pack(side=LEFT)
#            display(self.frame_table,self.table_image)
            display(self.frame_ordi,self.ordi_image)
            lbl1=make_label(self.frame_joeur1,self.image1,0,0)
            lbl1.grid(row=0,column=0)
            lbl2=make_label(self.frame_joeur2,self.image2,0,0)
            lbl2.grid(row=0,column=0)
            lbl3=make_label(self.frame_joeur3,self.image3,0,0)
            lbl3.grid(row=0,column=0)

    def change(self,frame,new_liste):
        self.clear_frame(frame)   
        display(frame,new_liste)

    def clear_frame(self,frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def clique_choix(self,carte,frame):
        self.dernier,self.table = tour(carte,self.table,self.joeur)
        self.dernier,self.table = tour_ordi(self.ordi,self.table)
        self.table_image = convert_image(self.table.cards)
        self.ordi_image = convert_image(self.ordi.cards)
        self.change(self.frame_table,self.table_image)
        self.change(self.frame_ordi,self.ordi_image)
        self.clear_frame(frame)
        if self.joeur.leng_cards()==0:
            self.table, self.joeur, self.ordi = distribuer(paquet,self.table,self.joeur,self.ordi)
            affichage=Affichage(jeu,paquet,self.table,self.joeur,self.ordi)
            affichage.change_show(jeu,affichage.ordi,affichage.carte1,affichage.carte2,affichage.carte3)
            #points_ordi = self.ordi.points
            #points_joeur = self.joeur.points

            n_car_j= affichage.joeur.leng_gain()
            n_car_o= affichage.ordi.leng_gain()
            if affichage.joeur.points < 41 and  affichage.ordi.points < 41:       

                # donner les cartes de la table au gagnant a la fin
                if affichage.dernier == "j":
                    for carte in affichage.table.cards:
                        affichage.joeur.gain_cards.append(carte)
                        affichage.table.remove_card(carte)

                    n_car_j = affichage.joeur.leng_gain() 
                    #dernier = f"les {table.leng_cards()} cartes de la table pour vous "
                if affichage.dernier == "o":
                    for carte in affichage.table.cards:
                        affichage.ordi.gain_cards.append(carte)
                        affichage.table.remove_card(carte)
                    n_car_o = ordi.leng_gain() 
                    #dernier = f"les  {table.leng_cards()} cartes de la table pour l'ordi "

                # compter les cartes recettes
                n_car_j= affichage.joeur.leng_gain()
                n_car_o= affichage.ordi.leng_gain()
                if n_car_j > 20:
                    affichage.joeur.points += (n_car_j-20)
                elif n_car_o > 20:
                    affichage.ordi.points += (n_car_o-20)


    def clear_frame_table(self,ordi,carte1,carte2,carte3):
        self.btn_simple.destroy()
        self.btn_complet.destroy()
        self.show(jeu)
        self.change_show(jeu,ordi,carte1,carte2,carte3)
        



jeu = tk.Tk()
jeu.geometry("800x700")
jeu["bg"]="SkyBlue"
paquet =Paquet()
joeur = Hand()
ordi = Hand()
table = Hand()
table, joeur, ordi = distribuer(paquet,table,joeur,ordi)
affichage = Affichage(jeu,paquet,table,joeur,ordi)
affichage.initial(jeu,affichage.ordi,affichage.carte1,affichage.carte2,affichage.carte3)
jeu.mainloop()
"""
def parti():

    class Affichage():
        def __init__(self,paquet=None,table=None,joeur=None,ordi=None):
            
            self.paquet = paquet
            self.ordi=ordi
            self.joeur=joeur
            self.carte1=self.joeur.cards[0]
            self.carte2=self.joeur.cards[1]
            self.carte3=self.joeur.cards[2]
            self.table=table
            self.table_image =convert_image(table.cards)
            self.ordi_image =convert_image(ordi.cards)
            self.image1=load_image(self.carte1)
            self.image2=load_image(self.carte2)
            self.image3=load_image(self.carte3)
            self.dernier =""

            self.frame_table = tk.Frame(jeu)
            self.frame_ordi = tk.Frame(jeu)
            self.frame_joeur1 = tk.Frame(jeu)
            self.frame_joeur2 = tk.Frame(jeu)
            self.frame_joeur3 = tk.Frame(jeu)
            self.lbl_points = tk.Label(jeu)
        def change(self,frame,new_liste):
            self.clear_frame(frame)   
            display(frame,new_liste)


        def clique_choix(self,carte,frame):
            self.dernier,self.table = tour(carte,self.table,self.joeur)
            self.dernier,self.table = tour_ordi(self.ordi,self.table)
            self.table_image = convert_image(self.table.cards)
            self.ordi_image = convert_image(self.ordi.cards)
            self.change(self.frame_table,self.table_image)
            self.change(self.frame_ordi,self.ordi_image)
            self.clear_frame(frame)
            if self.joeur.leng_cards()==0:
                self.win.destroy()
                self.table, self.joeur, self.ordi = distribuer(paquet,self.table,self.joeur,self.ordi)
                affichage=Affichage(paquet,self.table,self.joeur,self.ordi)
                affichage.affiche_initial(affichage.joeur,affichage.ordi)
                #points_ordi = self.ordi.points
                #points_joeur = self.joeur.points

                n_car_j= affichage.joeur.leng_gain()
                n_car_o= affichage.ordi.leng_gain()
                if affichage.joeur.points < 41 and  affichage.ordi.points < 41:       

                    # donner les cartes de la table au gagnant a la fin
                    if affichage.dernier == "j":
                        for carte in affichage.table.cards:
                            affichage.joeur.gain_cards.append(carte)
                            affichage.table.remove_card(carte)

                        n_car_j = affichage.joeur.leng_gain() 
                        #dernier = f"les {table.leng_cards()} cartes de la table pour vous "
                    if affichage.dernier == "o":
                        for carte in affichage.table.cards:
                            affichage.ordi.gain_cards.append(carte)
                            affichage.table.remove_card(carte)
                        n_car_o = ordi.leng_gain() 
                        #dernier = f"les  {table.leng_cards()} cartes de la table pour l'ordi "

                    # compter les cartes recettes
                    n_car_j= affichage.joeur.leng_gain()
                    n_car_o= affichage.ordi.leng_gain()
                    if n_car_j > 20:
                        affichage.joeur.points += (n_car_j-20)
                    elif n_car_o > 20:
                        affichage.ordi.points += (n_car_o-20)
            


        def affiche_initial(self,joeur,ordi):
            self.win = tk.Toplevel(jeu)
            self.win.geometry("800x700")
            self.win["bg"]= "SkyBlue2"
            self.win["relief"] = "raised"
            points_ordi = ordi.points
            points_joeur = joeur.points

            if paquet.leng_cards()==0:
                mssg=""
                if self.joeur.points > self.ordi.points:
                    mssg = f" Bravo vous avez gagné {self.joeur.points} contre {self.ordi.points}"                            
                elif self.ordi.points > self.joeur.points:
                    mssg = f" vous avez perdu {self.joeur.points} contre {self.ordi.points}" 
                else:
                    mssg = f"Égalité {self.joeur.points} contre {self.ordi.points}"  

                frame0=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                frame0.pack(side=BOTTOM)
                btn_quit= tk.Button(frame0, text="Quit", command=self.win.destroy,bg="SkyBlue2")
                btn_quit.grid(row=1,column=0)
                frame3=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                frame3.pack(side=TOP)        
                frame4=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                frame4.pack(side=BOTTOM)        
                frame5=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                frame5.pack(side=TOP)
                frame6=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                frame6.pack(side=BOTTOM)
                lbl_table=tk.Label(frame3,font=("courier",10),text=f"Sommaire de la partie    ",bg="SkyBlue2").pack()
                self.lbl_points=tk.Label(frame4,font=("courier",10),text=f"Les points de la partie : Ordi {self.ordi.points}  Vous : {self.joeur.points}",bg="SkyBlue2").pack()
                lbl_joeur=tk.Label(frame5,font=("courier",20),text=mssg).pack()
                lbl_paquet=tk.Label(frame6,font=("courier",10),text=f"Les cartes restantes :    {self.paquet.leng_cards()}",bg="SkyBlue2" ).pack()
            else:

                frame0=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                frame0.pack(side=BOTTOM)
                frame_joeur=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                frame_joeur.pack(side=BOTTOM)
                btn_quit= tk.Button(frame0, text="Quit", command=self.win.destroy,bg="SkyBlue2")
                btn_quit.grid(row=1,column=0)
                self.frame_joeur1=tk.Frame(frame_joeur,padx=40,pady=20,bg="SkyBlue2")
                self.frame_joeur1.pack(side=LEFT)
                self.frame_joeur2=tk.Frame(frame_joeur,padx=40,pady=20,bg="SkyBlue2")
                self.frame_joeur2.pack(side=LEFT)
                self.frame_joeur3=tk.Frame(frame_joeur,padx=40,pady=20,bg="SkyBlue2")
                self.frame_joeur3.pack(side=LEFT)
                frame3=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                frame3.pack(side=TOP)        
                self.frame_table=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                self.frame_table.pack(expand=True,side=TOP,fill=BOTH)        
                self.frame_ordi=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                self.frame_ordi.pack(expand=True,side=TOP,fill=BOTH)        
                lbl1=make_label(self.frame_joeur1,self.image1,0,0)
                lbl1.grid(row=0,column=0)
                lbl2=make_label(self.frame_joeur2,self.image2,0,0)
                lbl2.grid(row=0,column=0)
                lbl3=make_label(self.frame_joeur3,self.image3,0,0)
                lbl3.grid(row=0,column=0)
                btn1 = tk.Button(self.frame_joeur1,text="choix1",bg="SkyBlue2",command=partial(self.clique_choix,self.carte1,self.frame_joeur1))
                btn1.grid(row=0,column=1)
                btn2 = tk.Button(self.frame_joeur2,text="choix2",bg="SkyBlue2",command=partial(self.clique_choix,self.carte2,self.frame_joeur2))
                btn2.grid(row=0,column=1)
                btn3 = tk.Button(self.frame_joeur3,text="choix3",bg="SkyBlue2",command=partial(self.clique_choix,self.carte3,self.frame_joeur3))
                btn3.grid(row=0,column=1)
                frame4=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                frame4.pack(side=BOTTOM)        
                frame5=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                frame5.pack(side=BOTTOM)
                frame6=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
                frame6.pack(side=BOTTOM)
                lbl_table=tk.Label(frame3,font=("courier",10),text=f"cartes de la table     ",bg="SkyBlue2").pack()
                lbl_points=tk.Label(frame4,font=("courier",10),text=f"Les points de la partie :   Ordi {points_ordi}           Vous : {points_joeur}").pack()
                lbl_joeur=tk.Label(frame5,font=("courier",10),text=f"Les cartes gagnées de la partie :   Ordi : {self.ordi.leng_gain()}  Vous : {self.joeur.leng_gain()}  ")
                lbl_joeur.grid(row=0,column=1)
                lbl_paquet=tk.Label(frame6,font=("courier",10),text=f"Les cartes restantes :           paquet : {self.paquet.leng_cards()}" ).pack()
                display(self.frame_table,self.table_image)
                display(self.frame_ordi,self.ordi_image)
                lbl1=make_label(self.frame_joeur1,self.image1,0,0)
                lbl1.grid(row=0,column=0)
                lbl2=make_label(self.frame_joeur2,self.image2,0,0)
                lbl2.grid(row=0,column=0)
                lbl3=make_label(self.frame_joeur3,self.image3,0,0)
                lbl3.grid(row=0,column=0)
                
        def affiche_sommaire(self,joeur,ordi):
            self.win = tk.Toplevel(jeu)
            self.win.geometry("800x600")
            self.win["bg"]= "SkyBlue2"
            self.win["relief"] = "raised"
            points_ordi = ordi.points
            points_joeur = joeur.points

            frame0=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
            frame0.pack(side=BOTTOM)
            btn_quit= tk.Button(frame0, text="Quit", command=self.win.destroy,bg="SkyBlue2")
            btn_quit.grid(row=1,column=0)
            frame3=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
            frame3.pack(side=TOP)        
            frame4=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
            frame4.pack(side=BOTTOM)        
            frame5=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
            frame5.pack(side=BOTTOM)
            frame6=tk.Frame(self.win,padx=40,pady=20,bg="SkyBlue2")
            frame6.pack(side=BOTTOM)
            lbl_table=tk.Label(frame3,font=("courier",10),text=f"cartes de la table     ",bg="SkyBlue2").pack()
            lbl_points=tk.Label(frame4,font=("courier",10),text=f"Les points de la partie :   Ordi {points_ordi}           Vous : {points_joeur}").pack()
            lbl_joeur=tk.Label(frame5,font=("courier",10),text=f"Les cartes gagnées de la partie :   Ordi : {self.ordi.leng_gain()}  Vous : {self.joeur.leng_gain()}  ")
            lbl_joeur.grid(row=0,column=1)
            lbl_paquet=tk.Label(frame6,font=("courier",10),text=f"Les cartes restantes :           paquet : {self.paquet.leng_cards()}" ).pack()

    n_car_j, n_car_o = 0,0
    paquet =Paquet()
    joeur = Hand()
    ordi = Hand()
    table = Hand()
    table, joeur, ordi = distribuer(paquet,table,joeur,ordi)
    affichage=Affichage(paquet,table,joeur,ordi)
    affichage.affiche_initial(affichage.joeur,affichage.ordi)
def explication():
        fen = tk.Toplevel(jeu)
        fen.geometry("800x600")
        fen["bg"]= "SkyBlue2"
        fen["relief"] = "raised"
        f=open("explication.txt","r")
        mssg = f.read()
        f.close()
        #m=mssg  
        btn_quit= tk.Button(fen, text="Quit", command=fen.destroy,bg="SkyBlue2")
        btn_quit.grid(row=0,column=0)
        text_area = st.ScrolledText(fen,width = 70,height = 25,font = ("Times New Roman",15))
        text_area.grid(column = 0, pady = 20, padx = 25)
        # Inserting Text which is read only
        text_area.insert(tk.INSERT,mssg)
        text_area.configure(state ='disabled')
"""




