import tkinter as tk
import random as rd

class AppliCanevas(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = 500
        self.creer_widgets()

    def creer_widgets(self):
        # création canevas
        self.canv = tk.Canvas(self, bg="light gray", height=self.size,
                              width=self.size)
        self.canv.pack(side=tk.LEFT)
        
        # boutons
        self.bouton_oval = tk.Button(self, text="Cercle !",
                                        command=self.oval)
        self.bouton_oval.pack(side=tk.TOP)

        self.bouton_cercles = tk.Button(self, text="Cercle !",
                                        command=self.dessine_cercles)
        self.bouton_cercles.pack(side=tk.TOP)
        self.bouton_lignes = tk.Button(self, text="Lignes !",
                                       command=self.dessine_lignes)
        self.bouton_lignes.pack()
        self.bouton_quitter = tk.Button(self, text="Quitter",
                                        command=self.quit)
        self.bouton_quitter.pack(side=tk.BOTTOM)

    def rd_col(self):
        return rd.choice(("black", "red", "green", "blue", "yellow", "magenta",
                          "cyan", "white", "purple"))

    def dessine_cercles(self):
        for i in range(20):
            x, y = [rd.randint(1, self.size) for j in range(2)]
            diameter = rd.randint(1, 50)
            self.canv.create_oval(x, y, x+diameter, y+diameter,
                                  fill=self.rd_col())

    def dessine_lignes(self):
        for i in range(20):
            x, y, x2, y2 = [rd.randint(1, self.size) for j in range(4)]
            self.canv.create_line(x, y, x2, y2, fill=self.rd_col())
    def oval(self):
        self.canv.create_oval(0, 0, 200, 200, outline="red", width=10)
        self.canv.create_line(0, 0, 200, 200, fill="black", width=10)
        self.canv.create_line(0, 200, 200, 0, fill="black", width=10)

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = 5000
        self.creer_widgets()

    def creer_widgets(self):
        self.label = tk.Label(self, text="J'adore Python !")
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.canv = tk.Canvas(self, bg="white", height=200, width=200)
        self.canv.create_oval(0, 0, 200, 200, outline="red", width=10)
        self.canv.create_line(0, 0, 200, 200, fill="black", width=10)
        self.canv.create_line(0, 200, 200, 0, fill="black", width=10)
        self.label.pack(side=tk.TOP)
        self.bouton.pack(side =tk.BOTTOM)
        self.canv.pack(side=tk.LEFT)


if __name__ == "__main__":
    app = AppliCanevas()
    app.title("Mon Canevas Psychédélique !")
    app.mainloop()

