## Harris Corner Detector

### Summary
[Harris Corner Detector](https://en.wikipedia.org/wiki/Harris_Corner_Detector) is a corner detection algorithm that is commonly used in computer vision
algorithms to extract corners and infer the features of an image.
A corner is a point whose local neighbourhood stands in two dominant and different edge directions. In easy words we can say a corner is a junction of two edges, where an edge is a sudden change in image brightness.</br>
We have used [Sobel Operator](https://en.wikipedia.org/wiki/Sobel_operator) to extract the edges from the input image.
We have implemented the Harris Corner Detection by two ways.
1. [Without using any Direct API](https://github.com/rushirg/ComputerVision/blob/master/CornerDetection/HarrisCornerDetector.py)(Only with numpy)
2. [Using API from OpenCV module](https://github.com/rushirg/ComputerVision/blob/master/CornerDetection/HarrisCornerDetector_OpenCV.py)

### Installation
Make sure Python is installed on your system.</br>
if Python is not installed then use the following command lines to install for <b>Ubuntu</b>
1. ```apt update && apt upgrade -y```
2. ```apt install python3.6```


Also check if you have following packages installed on your system
1. ```cv2```
2. ```numpy```</br>
if not, install using </br>
```pip install <package-name>```

### Execute
Run:</br>
Execute implementation without any direct API call : ```python HarrisCornerDetector.py``` </br>
Excute with build-in API from OpenCV : ```python HarrisCornerDetector_OpenCV.py```</br>

### Result
Input Image</br>
<img src="/CornerDetection/input2.jpg" alt="Input Image" title="Input Image" width="394" height="331"></br></br>
Detected Corners</br>
<img src="/CornerDetection/harrisCornerOutput.jpg" alt="Detected Corners" title="Detected Corners"  width="394" height="331">


