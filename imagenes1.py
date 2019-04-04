__author__ = 'fhca'

import numpy as np
import matplotlib.pyplot as plt
"""
img = np.zeros((8, 8))
img[0:8:2, 1:8:2] = 1
img[1:8:2, 0:8:2] = 1
"""

img = np.zeros((80, 80))

for r in range(0, 80, 20):
    for c in range(10, 80, 20):
        img[r:r + 10, c:c + 10] = 1
        img[c:c + 10, r:r + 10] = 1
        # img[r+10:r+20, c-10:c] = 1


"""
# img += img.T

"""
img[0:10, 10:20] = 1
img[0:10, 30:40] = 1
img[0:10, 50:60] = 1
img[20:30, 10:20] = 1
img[20:30, 30:40] = 1
img[20:30, 50:60] = 1

img[10:20, 0:10] = 1
img[10:20, 20:30] = 1
img[10:20, 40:50] = 1
img[30:40, 0:10] = 1
img[30:40, 20:30] = 1
img[30:40, 40:50] = 1
"""
plt.figure()
plt.imshow(img)
plt.show()
