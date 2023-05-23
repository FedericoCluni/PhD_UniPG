import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


import numpy as np
from mod_int import integra

class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(column=0, row=0)
        self.create_menu()
        self.create_var()
        self.create_widgets()
    
    def create_menu(self):
        menubar = tk.Menu(self.master)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)

    def about(self):
        messagebox.showinfo(title="About",message="Made by Federico Cluni!")
        
    def checkfloat(self, input_text):
        #if not input_text:
        #    return True
        try:
            float(input_text)
            return True
        except ValueError:
            return False

    def create_var(self):
        self.m = tk.StringVar()
        self.m.set(str(1))
        self.b = tk.StringVar()
        self.b.set(str(0))
        self.x1 = tk.StringVar()
        self.x1.set(str(0))
        self.x2 = tk.StringVar()
        self.x2.set(str(1))
        self.I = tk.StringVar()
        
    def create_widgets(self):
        Fr_com = ttk.Frame(self)
        self.int_png = tk.PhotoImage(file="int.gif")
        
        ttk.Label(Fr_com, text="Evaluate the integral between x\u2081 and x\u2082 of the function\nf(x) = m x + b", 
            image=self.int_png, compound="bottom", width=50, anchor=tk.CENTER).grid(row=0, column=0, columnspan=2)
        
        check_cmd = self.register(self.checkfloat)
        
        ttk.Label(Fr_com, text="m", width=10, anchor=tk.W).grid(row=1, column=0)
        ttk.Entry(Fr_com, textvariable = self.m, validate='key', validatecommand=(check_cmd, '%P')).grid(row=1, column=1)
        
        ttk.Label(Fr_com, text="b", width=10, anchor=tk.W).grid(row=2, column=0)
        ttk.Entry(Fr_com, textvariable = self.b).grid(row=2, column=1)
        
        ttk.Label(Fr_com, text="x\u2081", width=10, anchor=tk.W).grid(row=3, column=0)
        ttk.Entry(Fr_com, textvariable = self.x1).grid(row=3, column=1)
        
        ttk.Label(Fr_com, text="x\u2082", width=10, anchor=tk.W).grid(row=4, column=0)
        ttk.Entry(Fr_com, textvariable = self.x2).grid(row=4, column=1)
                
        ttk.Button(Fr_com,text="Evaluate",  command=self.calcola).grid(row=5, column=0, columnspan=2)
        
        ttk.Label(Fr_com, text="Result", width=10, anchor=tk.W).grid(row=6, column=0)
        ttk.Label(Fr_com, textvariable=self.I).grid(row=6, column=1)
        
        Fr_com.grid(row=0, column=0, sticky=tk.N)
        # ---------------------------------------------------------------------------
        Fr_fig = ttk.Frame(self)
        
        self.disegna(Fr_fig)

        Fr_fig.grid(row=0, column=1)
        # ---------------------------------------------------------------------------
        self.master.bind('<Return>', self.calcola)
    
    def disegna(self, frame):
        fig = Figure(figsize=(5,4))
        ax = fig.add_subplot(111)
        
        m = float(self.m.get())
        b = float(self.b.get())
        x1 = float(self.x1.get())
        x2 = float(self.x2.get())
        x = np.linspace(x1,x2,100)
        y = m*x+b
        self.line, = ax.plot(x,y)
        ax.set_xlabel("$x$")
        ax.set_ylabel("$m\cdot x + b$")
        ax.grid(True)
       
        self.canvas = FigureCanvasTkAgg(fig,master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
        
        toolbar = NavigationToolbar2Tk(self.canvas, frame)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def calcola(self,*args):
        try:
            m = float(self.m.get())
            b = float(self.b.get())
            x1 = float(self.x1.get())
            x2 = float(self.x2.get())
        except ValueError:
            self.errori()
        else:
            I = integra(m, b, x1, x2)
            self.I.set(str(I))
            x = np.linspace(x1,x2,100)
            y = m*x+b
            self.line.set_ydata(y )
            self.canvas.draw()
    
    def errori(self):
        messagebox.showerror(title="Error!",message="Value not valid!")


root = tk.Tk()
root.title("Example tk")
app = App(master=root)
root.mainloop()