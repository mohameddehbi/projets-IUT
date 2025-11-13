# -*- coding: utf-8 -*-
"""
Exemple 45

@author: ADMIN
"""
import sympy as sm 
from sympy.abc import x,y 
eq1= sm.Eq (3*x+1*y, 2) 
eq2= sm.Eq (1*x-1*y, 1)
eq3= sm.Eq (-2*x+3*y, 2)
print (sm.solve([eq1,eq2,eq3]))
