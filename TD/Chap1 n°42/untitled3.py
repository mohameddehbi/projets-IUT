import numpy as np
M=[[2,12,15],
   [4,10,11],
   [5,9,9]]

n=[10,8,7]

# Determinant , si il est différent de 0 alors c'est inversible
sol1 = np.linalg.det(M)
print(sol1)
#Or ici le déterminant n'est pas égal à 0 donc le système est inversible

# Matrice Inverse
sol = np.linalg.inv(M)
print(sol)
print("----------------------------------------------")
V=[10,8,7]
print(sol*V)