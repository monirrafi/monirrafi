import tkinter as tk
import random
from tkinter import BOTH, BOTTOM, LEFT, RIGHT, TOP, messagebox
from turtle import left, right
from PIL import Image, ImageTk
from functools import partial



class Affichage:
    def __init__(self,table,joeur):
        self.table =table
        self.joeur =joeur
def display(master,liste):
    if len(liste)>16:
        for j in range(len(liste)//2+1):
                label=make_label(master,liste[j],0,j)
        for j in range(len(liste)//2):
                label=make_label(master,liste[j+len(liste)//2+1],1,j)
    else:
        for j in range(len(liste)):
                label=make_label(master,liste[j],0,j)
        
jeu = tk.Tk()
#fenrw = fen.winfo_reqwidth()
#fenrh = fen.winfo_reqheight()
#sw = fen.winfo_screenwidth()
#sh = fen.winfo_screenheight()
#fen.geometry("%dx%d+%d+%d" % (fenrw, fenrh, (sw-fenrw)/2, (sh-fenrh)/2))
jeu.geometry("500x200")
def load_image(ima):
    return ImageTk.PhotoImage(Image.open(ima))

im = load_image('ray1.PNG')
pas_im = load_image('ray2.PNG')
a=[im,im]
b=[im,pas_im,pas_im]

table =[im,pas_im,pas_im,im,im,pas_im,pas_im,im,im,pas_im,pas_im,im,im]
joeur =[im,im,im]

affichage = Affichage(table,joeur)


def make_label(master, ima,i,j):
    label= tk.Label(master,image=ima,relief=tk.RAISED,borderwidth=1)
    label.image=ima
    label.grid(row=i,column=j)
    return label
def create():
    win = tk.Toplevel(jeu)
    win.geometry("1000x800")
    win["bg"]= "SkyBlue2"
    win["relief"] = "raised"
    frame0=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
    frame0.pack(side=BOTTOM)
    btn1 = tk.Button(frame0,text="choix1", command=jeu.destroy,bg="SkyBlue2")
    btn1.grid(row=0,column=0)
    btn2 = tk.Button(frame0,text="choix2", command=jeu.destroy,bg="SkyBlue2")
    btn2.grid(row=0,column=1)
    btn_quit= tk.Button(frame0, text="Quit", command=win.destroy,bg="SkyBlue2")
    btn_quit.grid(row=1,column=0)
    frame3=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
    frame3.pack(side=TOP)        
    frame4=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
    frame4.pack(side=BOTTOM)        
    frame5=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
    frame5.pack(side=BOTTOM)
    frame2=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
    frame2.pack(side=BOTTOM)
    frame1=tk.Frame(win,padx=40,pady=20,bg="SkyBlue2")
    frame1.pack(side=TOP)        

    
    
            
    points_ordi = 13
    points_joeur = 21
    lbl_table=tk.Label(frame3,font=("courier",30),text="cartes de la table ",bg="SkyBlue2").pack()
    lbl_points=tk.Label(frame4,font=("courier",20),text=f"Ordi points : {points_ordi}           vos points : {points_joeur}").pack()
    lbl_joeur=tk.Label(frame5,font=("courier",30),text=f"vos cartes ",bg="SkyBlue2")
    lbl_joeur.grid(row=0,column=1)

    display(frame1,affichage.table)
    display(frame2,affichage.joeur)

    def change(frame1,tabl):
        affichage.table=tabl
        frame1.destroy()
        frame1=tk.Frame(win,padx=40,pady=20)
        frame1.pack(side=TOP)        
        display(frame1,affichage.table)
        
    btn3 = tk.Button(frame0,text="choix3", command=partial(change,frame1,b),bg="SkyBlue2")
    btn3.grid(row=0,column=2)
btn_simple = tk.Button(jeu, text="Jeu simple vainceur qui gagne une partie ", command = create).pack(pady=10)
btn_complet = tk.Button(jeu, text="Jeu compet vainceur qui atteint 41 points", command = create).pack(pady=10)
btn_quitter=tk.Button(jeu, text="Quit", command=jeu.destroy).pack(pady=10) 
jeu.mainloop()