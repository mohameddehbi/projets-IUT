import numpy as np

M=[[0,1,0,0,0,1],
   [0,1,0,0,1,0],
   [0,1,0,1,0,0],
   [0,0,1,0,0,1],
   [1,1,1,0,0,0],
   [0,0,0,1,1,1]]

n=[11,6,13,13,15,15]

# Determinant , si il est différent de 0 alors c'est inversible
sol1 = np.linalg.det(M)

# Matrice inverse
sol2 = np.linalg.inv(M)

# Solution du système
sol3 = np.linalg.solve(M,n)