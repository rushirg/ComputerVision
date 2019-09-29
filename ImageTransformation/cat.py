"""
Assignment: Programming Assignment 1 - Problem 1
            (Rotation, Translation, and Scaling of an Image)

Author: Rushikesh Gaidhani(5036426)

Class: Computer Vision (CAP 5415)
Instructor: Dr. Abhijit Mahalanobis
"""
import cv2
import math
import numpy as np
import logging


def rotateImage(image, row, column,):
    """Rotate an image with given angle, counterclockwise rotation if postive angle or else clockwise
    Args:
        image - image ndarray loaded from file
        row - number of rows in loaded image
        column - number of columns in loaded image
    """
    # Get input and convert the angle in degree to radians
    angle_rad = math.radians(int(input("Enter rotation angle: ")))

    # Initialize new image with zero
    newImage = np.zeros((2 * row, 2 * column, 3), dtype=np.uint8)

    # Calculate the sin and cos
    c, s = math.cos(angle_rad), math.sin(angle_rad)

    # Get the floor of the mid co-ordinates of original image
    mid_coords = np.floor(0.5 * np.array(image.shape))

    # Apply the equation for x2 and y2 to get the new co-ordinates with respect to mid coordinates
    for i in range(0, row - 1):
        for j in range(0, column - 1):
            x2 = mid_coords[0] + (i - mid_coords[0]) * \
                c - (j - mid_coords[1]) * s
            y2 = mid_coords[1] + (i - mid_coords[0]) * \
                s + (j - mid_coords[1]) * c
            newImage[int(round(x2) + 50), int(round(y2) + 50)] = image[i, j]

    # Save the image
    logging.info("Output image of rotated imagw by angle {} saved as output1.png".format(
        int(math.degrees(angle_rad))))
    cv2.imwrite("output1.png", newImage)


def translationImage(image, row, column):
    """Translation of matrix with reference to tx and ty
    Args:
        image - image ndarray loaded from file
        row - number of rows in loaded image
        column - number of columns in loaded image
    """

    # Get input for x and y for translation
    tx = int(input("Enter translation value for X: "))
    ty = int(input("Enter translation value for Y: "))
    xNew = row + abs(tx)
    yNew = column + abs(ty)

    # Create new image with zero
    newImage = np.zeros([xNew, yNew, 3])

    # Translate the original image to new position
    for i in range(row - 1):
        for j in range(column - 1):
            newImage[i + tx][j + ty] = image[i][j]

    # Save the image
    logging.info(
        "Output image for translating X by {x} and Y by {y} saved as output2.png".format(x=tx, y=ty))
    cv2.imwrite('output2.png', newImage)


def scalingImage(image, row, column):
    """Scale an image with reference to X and Y
    Args:
        image - image ndarray loaded from file
        row - number of rows in loaded image
        column - number of columns in loaded image
    """

    # Get scaling value for X and Y
    Sx = float(input("Enter scaling parameter(Sx) for X: "))
    Sy = float(input("Enter scaling parameter(Sy) for Y: "))

    # Calculate new height and width
    xNew = int(row * Sx)
    yNew = int(column * Sy)

    # Calculate the scale along x and y
    xScale = xNew / (row - 1)
    yScale = yNew / (column - 1)

    # Create new image
    newImage = np.zeros([xNew, yNew, 3])

    # Apply the scaling on the new image
    for i in range(xNew - 1):
        for j in range(yNew - 1):
            newImage[i + 1, j + 1] = image[1 +
                                           int(i / xScale), 1 + int(j / yScale)]

    # Save the image
    logging.info(
        "Output image for Scaling X by {x} and Y by {y} saved as output3.png".format(x=Sx, y=Sy))
    cv2.imwrite("output3.png", newImage)


def main():

    # Load image
    try:
        inputImage = cv2.imread('../data/image.png', 1)
        row, column, channel = inputImage.shape
    except IOError:
        print('Error while reading image.png')

    # Method call for rotate, translate, scale
    rotateImage(inputImage, row, column)
    translationImage(inputImage, row, column)
    scalingImage(inputImage, row, column)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
