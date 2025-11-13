# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 08:40:15 2022

@author: ADMIN
"""

import sympy as sm 
from sympy.abc import a,b
eq1= sm.Eq (2*a+3*b, 0)
eq2= sm.Eq (1*a+1*b, 0)
print (sm.solve([eq1,eq2],a,b))