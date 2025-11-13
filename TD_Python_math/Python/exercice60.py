# -*- coding: utf-8 -*-
"""
Exercice 60
Systeème non carré de 3 eq à 4 inconnues

@author: ADMIN
"""
import sympy as sm 
x,y,z,t=sm.symbols("x y z t")
A=sm.Matrix([[3,4,1,2],[6,2,2,5],[9,12,3,10]])
B=sm.Matrix([[3],[7],[13]])
X=sm.linsolve((A ,B),[x,y,z,t])
print ("L'ensemble des solutions du systèmes est S="+str(X))

