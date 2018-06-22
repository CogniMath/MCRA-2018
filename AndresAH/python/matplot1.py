import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0,1,0.01) * 5 * np.pi  # Eje x
y = np.sin(x)                        # Eje y

# Ahora graficamos

plt.figure(1,figsize=(12,9))
plt.plot(x,y,'--',color='red',linewidth=5)

plt.xlabel('x',fontsize=20)
plt.ylabel('sin(x)',fontsize=20)
plt.title('Ejemplo',fontsize=20)

plt.show()
