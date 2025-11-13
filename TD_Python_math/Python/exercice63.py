# -*- coding: utf-8 -*-
"""
Exercice 63

@author: ADMIN
"""
import sympy as sm 
x,y,z=sm.symbols("x y z")
A=sm.Matrix([[7,2,-1],[-3,-1,2],[1,0,3]])
B=sm.Matrix([[-3],[4],[5]])
X=sm.linsolve((A,B),[x,y,z])
print ("L'ensemble des solutions du systèmes est S="+str(X))
