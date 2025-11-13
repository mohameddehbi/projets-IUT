"""
Graphes
"""
import numpy as np
import matplotlib.pyplot as plt 
def f(x) :
    return -3*x**3-x**2
X= np.arange(-5,5,0.1)
Y=[ f(x) for x in X]
plt.plot(X,Y)