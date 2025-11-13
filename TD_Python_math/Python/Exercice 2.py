# -*- coding: utf-8 -*-
"""
Graphes de python
"""
import numpy as np
import matplotlib.pyplot as plt 
   
X= np.arange(-10,10,0.01)
Y=[ f(x) for x in X]
plt.plot(X,Y)


    