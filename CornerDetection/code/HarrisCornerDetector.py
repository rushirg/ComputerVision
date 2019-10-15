import cv2
import numpy as np
import argparse
import logging


def sobelEdgeOperator(img, rows, columns):
    """Get gradient images along x and y axis using sobel operator
    Args:
        img     - input grayscale image
        row     - number of rows in input image
        columns - number of columns in input image
    Returns:
        Ix  - derivative along x
        Iy  - derivative along y
    """
    # Sobel Operator
    Gx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    Gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    # Create empty images for gradient along x and y axis
    Ix = np.zeros((rows, columns))
    Iy = np.zeros((rows, columns))

    # Convolution Operation
    for i in range(0, rows - 3):
        for j in range(0, columns - 3):
            Ix[i, j] = (Gx * img[i:i + 3, j:j + 3]).sum()
            Iy[i, j] = (Gy * img[i:i + 3, j:j + 3]).sum()
    return Ix, Iy


def harrisCornerDetection(img, rows, columns, threshold, k):
    """Use harris corner detection algorithm to find corners in an image
    Args:
        img         - input grayscale image
        rows        - number of rows in image
        columns     - number of columns in image
        threshold   - theshold to find the cornerness
        k           - constant
    Return:
        img2    - image with detected corners
    """
    # Get respective gradient using sobel edge operator
    Ix, Iy = sobelEdgeOperator(img, rows, columns)

    # Get pixel by pixel product of gradient images
    Ixx = Ix * Ix
    Iyy = Iy * Iy
    Ixy = Ix * Iy

    # Window function
    w = np.ones((3, 3))

    # Get a copy of original image and conver to color channel image
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

    # Convolution Operation and fill circle for corner
    for i in range(0, rows - 3):
        for j in range(0, columns - 3):
            x = (w * Ixx[i:i + 3, j:j + 3]).sum()
            y = (w * Iyy[i:i + 3, j:j + 3]).sum()
            xy = (w * Ixy[i: i + 3, j:j + 3]).sum()
            R = (x * y - np.square(xy)) - k * np.square(x + y)
            if R > threshold:
                cv2.circle(img2, (j, i), 1, (0, 0, 255), -1)
    return img2


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=float, default=0.06, help="constant value use to square of trace matrix M")
    parser.add_argument("--threshold", type=int, default=100000000000, help="value to check corners")
    parser.add_argument("--inputImage", choices=["input.jpg", "input2.jpg"],
                        default="input.jpg", type=str, help="input image to find the corners")
    args = parser.parse_args()

    inputImagePath = "../images/{}".format(args.inputImage)
    outputImagePath = "../images/output/harrisCornerOutput.jpg"

    # Read image
    logging.info("Read input image from {}".format(inputImagePath))
    img = cv2.imread('{}'.format(inputImagePath), 0)

    # Get number of rows and columns
    rows = img.shape[0]
    logging.info("Number of rows: {}".format(rows))
    columns = img.shape[1]
    logging.info("Number of columns: {}".format(columns))

    # Harris Corner Detector
    logging.info("Using Harris Corner Detection Algorithm to find the corners in input image")
    resultImage = harrisCornerDetection(img, rows, columns, args.threshold, args.k)

    # Save output image
    logging.info("Saving output image as {}".format(outputImagePath))
    cv2.imwrite('{}'.format(outputImagePath), resultImage)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
