def integra(m, b, x1, x2):
    """Procedure to integrate between x1 and x2 
the function f(x) = m*x + b

  /\ x2
  |
  |  (m x + b) dx
  |
\/ x1

input arguments:
m: slope
b: intersection with y-axis
x1: left bound integration range
x2: right bound integration range
"""
    I = (m*x2**2/2+b*x2) - (m*x1**2/2+b*x1)
   
    return I