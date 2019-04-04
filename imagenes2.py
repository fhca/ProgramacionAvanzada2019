__author__ = 'fhca'

import matplotlib.pyplot as plt
import numpy as np

z = np.zeros((100, 100))

for x in range(100):
    for y in range(100):
        try:
            #z[x, y] = (x-50)**2+(y-50)**2
            z[x, y] = np.sin((x-50)*(y-50))/((x-50)*(y-50))
        except:
            pass

plt.figure()
plt.imshow(z)
plt.show()
