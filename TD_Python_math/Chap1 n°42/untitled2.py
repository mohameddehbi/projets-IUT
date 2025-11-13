import sympy as sm
import numpy as np
import scipy as sp
x,y,z,t=sm.symbols("x y z t")
A=sm.Matrix([[3,4,1,2],[6,2,2,5],[9,12,3,10]])
B=sm.Matrix([[3],[7],[13]])
X=sm.linsolve((A,B),[x,y,z,t])
print("Lensemble des solutions du système est S="+str(X))

print("\n")
print("---------------------Exercice 60----------------------------")
print("\n")

x,y,z=sm.symbols("x y z")
A=sm.Matrix([[1,-2,3],[4,2,2]])
B=sm.Matrix([[2],[5]])
X=sm.linsolve((A,B),[x,y,z])
print("Lensemble des solutions du système est S="+str(X))

print("\n")
print("---------------------Exercice 61----------------------------")
print("\n")

x,y,z=sm.symbols("x y z")
A=sm.Matrix([[2,2,-8],[4,-2,1],[2,1,-2],[10,19,1]])
B=sm.Matrix([[-3],[1],[-1],[-8]])
X=sm.linsolve((A,B),[x,y,z])
print("Lensemble des solutions du système est S="+str(X))

print("\n")

B2=sm.Matrix([[-3],[1],[-1],[8]])
X2=sm.linsolve((A,B2),[x,y,z])
print("Lensemble des solutions du système est S="+str(X2))

print("\n")
print("---------------------Exercice 62----------------------------")
print("\n")

M=np.array([[1/2,0,-1/2],
   [1/2,1,1/2],
   [-1/2,0,1/2]])
k=sp.linalg.null_space(M) # NOYAU DE M

im=sp.linalg.orth(M) # Donne les vecteurs de bases de l'image de M

print(k)
print("\n")
print(im)
print(np.linalg.matrix.rank(A))