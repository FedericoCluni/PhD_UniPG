import numpy as np
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt

from io import BytesIO
import base64
        
def integra(m, b, x1, x2):

    I = (m*x2**2/2+b*x2) - (m*x1**2/2+b*x1)
   
    return I
        
def compute(m, b, x1, x2):
 
    I = integra(m, b, x1, x2)
    x = np.linspace(x1,x2,100)
    y = m*x+b
    plt.figure(figsize=(8,4))  # needed to avoid adding curves in plot
    plt.plot(x, y, 'b')
    plt.xlabel("$x$")
    plt.ylabel("$m\cdot x + b$")
    plt.grid(True)

    # Make Matplotlib write to BytesIO file object and grab
    # return the object's string
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    figdata_png = base64.b64encode(figfile.getvalue())
    
    return figdata_png, I


