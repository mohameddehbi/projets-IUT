import numpy as np

# Coefficients du système d'équations
coefficients = np.array([[2, 12, 15],
                         [4, 10, 11],
                         [5, 9, 9]])

# Termes constants
constants = np.array([10, 8, 7])

# Résolution du système pour obtenir la solution unique
solution_unique = np.linalg.solve(coefficients, constants)
print("La solution unique du système est :", solution_unique)

# Ajout d'une variable arbitraire pour obtenir une deuxième solution
arbitrary_variable = 2  # Choisissons une valeur arbitraire, tu peux en choisir une autre
modified_constants = constants + arbitrary_variable * np.array([1, 1, 1])

# Résolution du système avec les termes constants modifiés pour obtenir une deuxième solution
solution_2 = np.linalg.solve(coefficients, modified_constants)
print("Une deuxième solution du système est :", solution_2)

print(modified_constants)