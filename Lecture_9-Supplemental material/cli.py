import sys

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

Insert values of m, b, x1 and x2 separated by spaces
"""

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(info)
    elif len(sys.argv) < 5:
        print("Insufficient arguments!")
    elif len(sys.argv) > 5:
        print("Too much arguments!")
    else:
        try:
            m = float(sys.argv[1])
            b = float(sys.argv[2])
            x1 = float(sys.argv[3])
            x2 = float(sys.argv[4])
        except ValueError:
            print("Values not valid!")
        else:
            I = integra(m, b, x1, x2)
            print(I)

