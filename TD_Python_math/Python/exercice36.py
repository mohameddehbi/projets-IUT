# -*- coding: utf-8 -*-
"""
Exercice36

@author: Tessie
"""
import numpy as np 

A=np.array([[2,3,7],[1,-1,6]]) 
print('la matrice A vaut :\n',A)

B=np.array([[1,2],[0,1],[2,0]])
print('la matrice B vaut :\n',B)

Z=np.zeros((2,3))
print('la matrice Z vaut :\n',Z)

Id=np.eye(2)
print('la matrice Id vaut :\n',Id)

print(2*A)
print('la matrice 2*A vaut :\n',2*A)

AT=A.transpose()
print('la matrice AT vaut :\n',AT)

print(A+Z)
print('la matrice A+Z vaut :\n',A+Z)

AB=np.dot(A,B)
print('la matrice AB vaut :\n',AB)

BA=np.dot(B,A)
print('la matrice BA vaut :\n',BA)

IdA=np.dot(Id,A)
print('la matrice IdA vaut :\n',IdA)

BId=np.dot(B,Id)
print('la matrice BId vaut :\n',BId)
