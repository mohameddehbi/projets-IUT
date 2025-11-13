import numpy as np

M=[[2,12,15],
   [4,10,11],
   [5,9,9]]

n=[10,8,7]

# Determinant , si il est différent de 0 alors c'est inversible
sol = np.linalg.det(M)

# Matrice inverse
#sol = np.linalg.inv(M)

# Solution du système
sol = np.linalg.solve(M,n)
