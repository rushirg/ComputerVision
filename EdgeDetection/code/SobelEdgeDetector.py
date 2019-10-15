"""
Sobel Edge Detector
"""
import cv2
import numpy as np
import logging
import argparse


def sobelEdgeDetector(img, rows, columns, threshold):
    """Apply Sobel Operator to a given image
    Args:
        img         - input gray scale image
        rows        - number of rows in input image
        columns     - number of columns in input image
        threshold   - threshold for resulted gradient magnitude, default=100
    Returns:
        mag     - gradient magnitude of the image
        x_comp  - horizontal derivative
        y_comp  - vertical derivative
    """
    # Sobel Kernels
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # Create Empty image for output, x component, and y component
    mag = np.zeros((rows, columns))
    x_comp = np.zeros((rows, columns))
    y_comp = np.zeros((rows, columns))

    # Convolution Operation
    for i in range(0, rows - 3):
        for j in range(0, columns - 3):
            S1 = (Gx * img[i:i + 3, j:j + 3]).sum()
            S2 = (Gy * img[i:i + 3, j:j + 3]).sum()
            x_comp[i, j] = S1
            y_comp[i, j] = S2
            magnitude = np.sqrt(S1**2 + S2**2)
            mag[i + 1, j + 1] = magnitude if magnitude > threshold else 0

    return mag, x_comp, y_comp


def main():

    # Get threshold value for gradient magnitude
    parser = argparse.ArgumentParser()
    parser.add_argument('--threshold', type=int, default=20,
                        help="Input threshold to apply on gradient magnitude of the image")
    args = parser.parse_args()

    inputImage = "../images/Valve_original.PNG"
    outputImagePath = "../images/output/"

    # Read input image
    logging.info("Read input image")
    img = cv2.cvtColor(cv2.imread(inputImage), cv2.COLOR_BGR2GRAY)

    # Get number of rows and columns
    rows = img.shape[0]
    logging.info("Number of rows: {}".format(rows))
    columns = img.shape[1]
    logging.info("Number of columns: {}".format(columns))

    # Sobel Edge Detector
    logging.info("Using Sobel Operator to find Edges")
    mag, x_comp, y_comp = sobelEdgeDetector(img, rows, columns, args.threshold)

    # Save Output Images
    logging.info("Saving output image for vertical derivative as {}verticalDerivative_x.PNG".format(outputImagePath))
    cv2.imwrite('{}verticalDerivative_x.PNG'.format(outputImagePath), x_comp)
    logging.info("Saving output image for horizontal derivative as {}horizontalDerivative_y.PNG".format(outputImagePath))
    cv2.imwrite('{}horizontalDerivative_y.PNG'.format(outputImagePath), y_comp)
    logging.info("Saving output image for gradient magnitude as {}gradientMagnitudeResult.PNG.".format(outputImagePath))
    cv2.imwrite('{}gradientMagnitudeResult.PNG'.format(outputImagePath), mag)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
