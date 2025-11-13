import matplotlib.pyplot as plt
import numpy as np

# Générer une liste de valeurs de y régulièrement espacées
y_values = np.linspace(-5, 5, 100)  # Vous pouvez ajuster l'intervalle [-5, 5] ici

# Calculer les valeurs correspondantes de x en utilisant l'équation x = 3 - 2y
x_values = 3 - 2 * y_values

# Tracé de la droite
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Droite : x + 2y = 3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphique de la droite : x + 2y = 3')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
