"""
Image Source: By Original full portrait: "Playmate of the Month". Playboy Magazine. November 1972, photographed by Dwight Hooker.This 512x512 electronic/mechanical scan of a section of the full portrait: Alexander Sawchuk and two others[1] - The USC-SIPI image database, Fair use, https://en.wikipedia.org/w/index.php?curid=20658476
"""

import cv2
import numpy as np

img = cv2.imread('input.jpg', 0)
operatedImage = img
operatedImage = np.float32(operatedImage) 
img2 = img.copy()
img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07) 
dest = cv2.dilate(dest, None)
img2[dest > 0.01 * dest.max()]=[0, 0, 255]
cv2.imwrite('input_Result.jpg', img2)
