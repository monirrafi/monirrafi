from cgitb import text
import tkinter as tk
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
#        self.geometry("500x600")
        self.creer_widgets()

    def creer_widgets(self):
        #self.label = tk.Label(self, text="J'adore Python !").pack(side=tk.TOP)
        self.bouton1 = tk.Button(self, text="1",padx=40,pady=20, command=self.button_add).grid(row=2,column=1)
        self.bouton2= tk.Button(self, text="2",padx=40,pady=20, command=self.button_add).grid(row=2,column=2)
        self.bouton3 = tk.Button(self, text="3",padx=40,pady=20, command=self.button_add).grid(row=2,column=3)

        self.bouton4 = tk.Button(self, text="4",padx=40,pady=20, command=self.button_add).grid(row=1,column=1)
        self.bouton5 = tk.Button(self, text="5",padx=40,pady=20, command=self.button_add).grid(row=1,column=2)
        self.bouton6 = tk.Button(self, text="6",padx=40,pady=20, command=self.button_add).grid(row=1,column=3)
 
        self.bouton7 = tk.Button(self, text="7",padx=40,pady=20, command=self.button_add).grid(row=0,column=1)
        self.bouton8 = tk.Button(self, text="8",padx=40,pady=20, command=self.button_add).grid(row=0,column=2)
        self.bouton9 = tk.Button(self, text="9",padx=40,pady=20, command=self.button_add).grid(row=0,column=3)

        self.bouton0 = tk.Button(self, text="0", padx=40,pady=20, command=self.button_add).grid(row=4,column=2)
        self.bouton_add = tk.Button(self, text="+", padx=40,pady=10, command=self.button_add).grid(row=4,column=1)
        self.bouton_mins = tk.Button(self, text="-", padx=40,pady=1, command=self.button_add).grid(row=4,column=3)
        self.bouton_equal = tk.Button(self, text="=", padx=40,pady=1, command=self.button_add).grid(row=5,column=3)
#        self.bouton_clear = tk.Button(self, text="C", padx=40,pady=20, command=self.button_add).grid(row=4,column=4)
    def button_add():
        return
#        self.my_image = tk.PhotoImage(file="ray2.png")
#        self.label.pack(side=tk.TOP)
#        self.bouton.pack(side =tk.BOTTOM)
 #       self.my_text = tk.Text(self,text="monir")
 #       self.my_text.pack(side=tk.TOP)
if __name__ == "__main__":
    app = Application()
    app.title("Mon Canevas Psychédélique !")
    app.mainloop()
