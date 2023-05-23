def integra(m, b, x1, x2):
    I = (m*x2**2/2+b*x2) - (m*x1**2/2+b*x1)
    return I


info = """Procedure to integrate between x1 and x2 
the function f(x) = m*x + b

  /\ x2
  |
  |  (m x + b) dx
  |
\/ x1
"""

def inserisci(var):
    v = input("insert %s: "%var)
    try:
        v = float(v)
    except ValueError:
        print("Value not valid!")
        return inserisci(var)
    else:
        return v

if __name__ == "__main__":

    print(info)
    m = inserisci("m")
    b = inserisci("b")
    x1 = inserisci("x1")
    x2 = inserisci("x2")
    I = integra(m, b, x1, x2)
    print("The integral is %f"%I)

