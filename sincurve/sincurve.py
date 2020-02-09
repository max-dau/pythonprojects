import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi)
plt.plot(x, np.sin(x))
plt.xlabel('Angle')
plt.ylabel('sin(Angle)')
plt.show()
