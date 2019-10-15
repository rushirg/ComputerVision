import cv2
import numpy as np
import argparse
import logging


def applyHarrisCorner(inputImg):
    """Find the Harris Corners from the imput image
    :param inputImg: Gray scale input image
    :return: image with detected corners in red circles
    """
    operatedImage = inputImg
    operatedImage = np.float32(operatedImage)

    # Convert an input image copy to mark the detected corners in red circles
    imgCopy = inputImg.copy()
    imgCopy = cv2.cvtColor(imgCopy, cv2.COLOR_GRAY2BGR)

    logging.info("Applying Harris Corner Detector using OpenCV")
    dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)
    dest = cv2.dilate(dest, None)
    imgCopy[dest > 0.01 * dest.max()] = [0, 0, 255]
    return imgCopy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputImage", choices=["input.jpg", "input2.jpg"],
                        default="input.jpg", type=str, help="input image to find the corners")
    args = parser.parse_args()

    inputImagePath = "../images/{}".format(args.inputImage)
    outputImagePath = "../images/output/input_OpenCV_result.jpg"

    logging.info("Reading input image from: {}".format(inputImagePath))
    img = cv2.imread(inputImagePath, 0)

    resultImage = applyHarrisCorner(img)

    logging.info("Saving output image path at: {}".format(outputImagePath))
    cv2.imwrite(outputImagePath, resultImage)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
