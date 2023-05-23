import tkinter as tk
import tkinter.ttk as ttk

from mod_int import integra

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
                
        self.m = tk.StringVar()
        self.b = tk.StringVar()
        self.x1 = tk.StringVar()
        self.x2 = tk.StringVar()
        self.I = tk.StringVar()
        
        self.create_gui()
        
        self.grid(column=0, row=0)
        
    def create_gui(self):
          
        Fr_com = tk.Frame(self)
        
        tk.Label(Fr_com, text="Evaluate the integral between x\u2081 and x\u2082 of the function\nf(x) = m x + b", 
                   ).grid(row=0, column=0, columnspan=2)
                
        tk.Label(Fr_com, text="m", width=10, anchor=tk.W).grid(row=1, column=0)
        tk.Entry(Fr_com, textvariable = self.m).grid(row=1, column=1)
        
        tk.Label(Fr_com, text="b", width=10, anchor=tk.W).grid(row=2, column=0)
        tk.Entry(Fr_com, textvariable = self.b).grid(row=2, column=1)
        
        tk.Label(Fr_com, text="x\u2081", width=10, anchor=tk.W).grid(row=3, column=0)
        tk.Entry(Fr_com, textvariable = self.x1).grid(row=3, column=1)
        
        tk.Label(Fr_com, text="x\u2082", width=10, anchor=tk.W).grid(row=4, column=0)
        tk.Entry(Fr_com, textvariable = self.x2).grid(row=4, column=1)
                
        tk.Button(Fr_com,text="Evaluate",  command=self.calcola).grid(row=5, column=0, columnspan=2)
        
        tk.Label(Fr_com, text="Result", width=10, anchor=tk.W).grid(row=6, column=0)
        tk.Label(Fr_com, textvariable=self.I).grid(row=6, column=1)
        
        Fr_com.grid(row=0, column=0, sticky=tk.N)
       
    def calcola(self,*args):
    
        m = float(self.m.get())
        b = float(self.b.get())
        x1 = float(self.x1.get())
        x2 = float(self.x2.get())
        I = integra(m, b, x1, x2)
        self.I.set(str(I))

root = tk.Tk()
root.title("Esempio tk")
app = App(master=root)
root.mainloop()
