# -*- coding: utf-8 -*-
"""
Exercice40

@author: Tessie
"""

import numpy as np

A=np.array([[1,6,4],[3,5,3],[5,4,6]])
print('la matrice A vaut :\n',A)

print('déterminant :',np.linalg.det(A))

B=np.array([[113],[102],[127]])
print('la matrice B vaut :\n',B)

X=np.linalg.solve(A,B)
print('solution:\n' ,X)

