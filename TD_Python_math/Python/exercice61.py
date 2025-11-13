# -*- coding: utf-8 -*-
"""
Exercice 61

@author: ADMIN
"""
import sympy as sm 
from sympy.abc import x,y,z 
eq1= sm.Eq (x-2*y+3*z, 2)
eq2= sm.Eq (4*x+2*y+2*z, 5)
print (sm.solve([eq1,eq2],x,y,z))
