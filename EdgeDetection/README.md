## Sobel Edge Detection

### Summary
[Sobel Operator](https://en.wikipedia.org/wiki/Sobel_operator) or Sobel Filter, is used in computer vision for edge detection. It is a 3x3 image gradient operator when convolving on the image gives image derivatives for horizontal change and for vertical change. 

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
Change the directory to code and then execute below</br>
Implementation without any direct API call : ```python SobelEdgeDetector.py``` </br>

### Result
Input Image</br>
<img src="/EdgeDetection/Valve_original.PNG" alt="Input Image" title="Input Image" width="320" height="240"></br></br>
Horizontal change</br>
<img src="/EdgeDetection/horizontalDerivative_y.PNG" alt="along y" title="Horizontal Change"  width="320" height="240"></br></br>
Vertical change</br>
<img src="/EdgeDetection/verticalDerivative_x.PNG" alt="along x" title="Vertical Change"  width="320" height="240"></br></br>
Sobel Operator applied to input Image</br>
<img src="/EdgeDetection/gradientMagnitudeResult.PNG" alt="result" title="Result Image"  width="320" height="240"></br>

## Image Credit
By Simpsons contributor, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=8904364 </br>
More details: https://en.wikipedia.org/wiki/Sobel_operator
