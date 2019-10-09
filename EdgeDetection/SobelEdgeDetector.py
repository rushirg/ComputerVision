"""
Sobel Edge Detector

Source Image Credit: By Simpsons contributor, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=8904364

More details: https://en.wikipedia.org/wiki/Sobel_operator
"""
import numpy as np
import cv2


img = cv2.cvtColor(cv2.imread('Valve_original.PNG'), cv2.COLOR_BGR2GRAY)
import pdb; pdb.set_trace()
rows = img.shape[0]
columns = img.shape[1]

Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

mag = np.zeros((rows, columns))

x_comp = np.zeros((rows, columns))
y_comp = np.zeros((rows, columns))

for i in range(0, rows - 3):
    for j in range(0, columns - 3):
        S1 = sum(sum(Gx * img[i:i + 3, j:j + 3]))
        S2 = sum(sum(Gy * img[i:i + 3, j:j + 3]))
        x_comp[i, j] = S1
        y_comp[i, j] = S2
        mag[i + 1, j + 1] = np.sqrt(S1 * S1 + S2 * S2)
cv2.imwrite('verticalDerivative_x.PNG', x_comp)
cv2.imwrite('horizontalDerivative_y.PNG', y_comp)
cv2.imwrite('gradientMagnitudeResult.PNG', mag)
