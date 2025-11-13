# -*- coding: utf-8 -*-
"""
Spyder Editor

Exercice 41
"""
import sympy as sm 
from sympy.abc import x,y,z 
eq1= sm.Eq (2*x+12*y+15*z, 150)
eq2= sm.Eq (4*x+10*y+11*z, 126)
eq3= sm.Eq (6*x+8*y+14*z, 130)
print (sm.solve([eq1,eq2,eq3]))