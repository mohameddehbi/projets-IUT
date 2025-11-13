# -*- coding: utf-8 -*-
"""
Exercice 50

@author: ADMIN
"""
import sympy as sm 
from sympy.abc import a,b,c 
eq1= sm.Eq (a+2*b+2*c, 0)
eq2= sm.Eq (-1*a+1*b+3*c, 0)
eq3= sm.Eq (0*a+0*b+1*c, 0)
print (sm.solve([eq1,eq2,eq3]))