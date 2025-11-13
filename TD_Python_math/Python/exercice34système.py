# -*- coding: utf-8 -*-
"""
Exercice 34 système

@author: Tessie
"""
import sympy as sm 
from sympy.abc import x,y,z 
eq1= sm.Eq (x+2*y+3*z, -1)
eq2= sm.Eq (3*x-3*y+z, 2)
eq3= sm.Eq (x-7*y-5*z, 4)
print (sm.solve([eq1,eq2,eq3]))
