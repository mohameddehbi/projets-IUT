# -*- coding: utf-8 -*-
"""
Exercice 27+28

@author: Tessie
"""
import numpy as np
def sommegeo(x,n):
    s= 1
    p= 1
    for k in range(n):
        p=p*x
        s=s+p
    return (s)
        