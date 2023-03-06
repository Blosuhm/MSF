import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# constants
CAR_KMH = 70
CAR_MS = 70 / 3.6
POLICE_MS2 = 2

# Range
TIME = np.arange(1, 30)

# Functions
POS_CAR = TIME * CAR_MS
POS_POLICE = (1 / 2) * POLICE_MS2 * TIME**2

figure, ax = plt.subplots(1)
ax.set_xlabel("tempo (s)")
ax.set_ylabel("posição (m)")
ax.plot(TIME, POS_CAR, label="Carro fugitivo")
ax.plot(TIME, POS_POLICE, label="Carro da policia")
ax.set_title("2 Carros")
plt.legend()
plt.grid()
plt.show()
