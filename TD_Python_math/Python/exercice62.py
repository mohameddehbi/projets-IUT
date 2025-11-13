# -*- coding: utf-8 -*-
"""
Exercice 62

@author: ADMIN
"""
import sympy as sm 
from sympy.abc import x,y,z
eq1= sm.Eq (7*x+2*y-1*z, -3) 
eq2= sm.Eq (-3*x-1*y+2*z, 4)
eq3= sm.Eq (1*x+3*z, 5)
print (sm.solve([eq1,eq2,eq3]))
