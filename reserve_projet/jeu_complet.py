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
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
class Card :
    suit_names = ["ray","ray","ray","ray"]
    rank_names = [None, "1", "2","1", "2","1", "2","1", "2","1", "2"]
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        
    def __str__(self) :
        return '%s_%s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def image(self):
        return Card.suit_names[self.suit] + Card.rank_names[self.rank] 
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



#    affichage(p_joeur,p_ordi,paquet,joeur,ordi,table,3,"")


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

    return dernier,table,joeur


def load_image(card):
    card_name = card.image()+".png"
    return ImageTk.PhotoImage(Image.open(card_name))
def convert_image(l):
    l_image=[]
    for carte in l:
        l_image.append(load_image(carte))
    return l_image
"""
im = ImageTk.PhotoImage(Image.open('ray1.PNG'))
pas_im = ImageTk.PhotoImage(Image.open('ray2.PNG'))

tableTetst =[im,pas_im,pas_im,im,im,pas_im,pas_im,im,im,pas_im,pas_im,im,im]
joeurTest =[im,im,im]
"""
def make_label(master, ima,i,j):
    label= tk.Label(master,image=ima,relief=tk.RAISED,borderwidth=1)
    label.image=ima
    label.grid(row=i,column=j)
    return label
def display(master,liste):
    if len(liste)>16:
        for j in range(len(liste)//2+1):
                label=make_label(master,liste[j],0,j)
        for j in range(len(liste)//2):
                label=make_label(master,liste[j+len(liste)//2+1],1,j)
    else:
        for j in range(len(liste)):
                label=make_label(master,liste[j],0,j)
class Affichage:
    def __init__(self,table,joeur):
        self.joeur=joeur
        self.table=table
        self.table_image =convert_image(table.cards)
        self.joeur_image =convert_image(joeur.cards)
        self.dernier =""


def affiche_initial():
    def change(master,liste,l_side):
        #master.destroy()
        master=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
        master.pack(side=l_side)        
        display(master,liste)

    def clique_choix1():
        r_dernier,r_table,r_joeur = tour(joeur.cards[0],affichage.table,affichage.joeur)
        r_dernier,r_table = tour_ordi(ordi,table)
        affichage.table=r_table
        affichage.joeur=r_joeur
        affichage.dernier=r_dernier
        affichage.table_image = convert_image(affichage.table.cards)
        affichage.joeur_image = convert_image(affichage.joeur.cards)
        frame_table.destroy()
        frame_table=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
        frame_table.pack(side=TOP)        
        display(frame_table,affichage.table_image)
        frame_joeur.destroy()
        frame_joeur=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
        frame_joeur.pack(side=TOP)        
        display(frame_joeur,affichage.joeur_image)

#        change(frame_table, affichage.table_image,TOP)
#        change(frame_joeur, affichage.joeur_image,BOTTOM)
        btn1.destroy()

    def clique_choix2():
        a=len(affichage.joeur.cards)
        r_dernier,r_table,r_joeur = tour(joeur.cards[0],affichage.table,affichage.joeur)
        r_dernier,r_table = tour_ordi(ordi,table)
        affichage.table=r_table
        affichage.joeur=r_joeur
        affichage.dernier=r_dernier
        affichage.table_image = convert_image(affichage.table.cards)
        affichage.joeur_image = convert_image(affichage.joeur.cards)
        frame_table.destroy()
        frame_table=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
        frame_table.pack(side=TOP)        
        display(frame_table,affichage.table_image)
        frame_joeur.destroy()
        frame_joeur=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
        frame_joeur.pack(side=TOP)        
        display(frame_joeur,affichage.joeur_image)
        btn2.destroy()
    def clique_choix3():
        affichage.dernier,affichage.table,affichage.joeur = tour(joeur.cards[0],affichage.table,affichage.joeur)
    #    affichage.dernier,affichage.table = tour_ordi(ordi,table)
        affichage.table_image = convert_image(affichage.table.cards)
        affichage.joeur_image = convert_image(affichage.joeur.cards)
        change(frame_table, affichage.table_image,TOP)
        change(frame_joeur, affichage.joeur_image,BOTTOM)
        btn3.destroy()


#    def return_pressed(event,card,table):
 #       clique_choix(card,table)

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
    display(frame_table,affichage.table_image)
    display(frame_joeur,affichage.joeur_image)

"""
    leng = paquet.leng_cards()
    if leng != 0:
        cond1 = False
        mssg =""
        while (not cond1):
            if leng== 0:
                cond1 = True 
            else:
                distribuer(paquet,table,joeur,ordi)
                table_image=convert_image(table.cards)
                joeur_image=convert_image(joeur.cards)
                affichage=Affichage(table_image,joeur_image)
                n_car_j, n_car_o = 0,0
                i=0
                while i<3:
    #                affichage(paquet,joeur,ordi,table,joeur.leng_cards())
                    if joeur.points >= 41 or ordi.points >= 41:
                        # return joeur.points, ordi.points
                        i=3

                    else:
                        affichage.btn1.bind("Button-1",lambda event:return_pressed(joeur.cards[0],table))
                        affichage.btn2.bind("Button-1",lambda event:return_pressed(joeur.cards[0],table))
                        affichage.btn3.bind("Button-1",lambda event:return_pressed(joeur.cards[0],table))
                    i+=1
        points_ordi = ordi.points
        points_joeur = joeur.points

        if joeur.points < 41 and  ordi.points < 41:       
            # donner les cartes de la table au gagnant a la fin
            if affichage.dernier == "j":
                n_car_j = joeur.leng_gain() +  table.leng_cards()
            if affichage.dernier == "o":
                n_car_o = ordi.leng_gain() +  table.leng_cards()
            # compter les cartes recettes
            if n_car_j > 20:
                joeur.points += (n_car_j-20)
            elif n_car_o > 20:
                ordi.points += (n_car_o-20)
"""
        
jeu = tk.Tk()
jeu.geometry("500x200")
joeur = Hand("j")
ordi = Hand("o")
table = Hand("t")
paquet =Paquet()
paquet.brasser()
distribuer(paquet,table,joeur,ordi)
affichage=Affichage(table,joeur)

 
       

    
    
btn_simple = tk.Button(jeu, text="Jeu simple vainceur qui gagne une partie ", command = affiche_initial).pack(pady=10)
btn_complet = tk.Button(jeu, text="Jeu compet vainceur qui atteint 41 points", command = affiche_initial).pack(pady=10)
btn_quitter=tk.Button(jeu, text="Quit", command=jeu.destroy).pack(pady=10) 
jeu.mainloop()