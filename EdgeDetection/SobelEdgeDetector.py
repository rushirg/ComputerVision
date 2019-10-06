"""
Sobel Edge Detector

Source Image Credit: By Simpsons contributor, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=8904364
"""
import matplotlib.image as mpimg
import numpy as np
import math


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


img = mpimg.imread('Valve_original.PNG')
gray = rgb2gray(img)
rows = gray.shape[0]
columns = gray.shape[1]

Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

mag = np.zeros((rows, columns))

x_comp = np.zeros((rows, columns))
y_comp = np.zeros((rows, columns))

for i in range(0, rows - 3):
    for j in range(0, columns - 3):
        S1 = sum(sum(Gx * gray[i:i + 3, j:j + 3]))
        S2 = sum(sum(Gy * gray[i:i + 3, j:j + 3]))
        x_comp[i, j] = S1
        y_comp[i, j] = S2
        mag[i + 1, j + 1] = math.sqrt(S1 * S1 + S2 * S2)
mpimg.imsave('verticalDerivative_x.PNG', x_comp)
mpimg.imsave('horizontalDerivative_y.PNG', y_comp)
mpimg.imsave('gradientMagnitudeResult.PNG', mag)
