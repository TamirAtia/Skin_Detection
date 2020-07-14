# Skin Detection
Python Final Project Skin Detection final project on Python and Computer vision course. Libraries: Opencv2, numpy, imutils

<a href="https://ibb.co/5M92Hr4"><img src="https://i.ibb.co/w0LYmSg/pic1.jpg" alt="pic1" border="0" /></a>

In this project we will deal with skin color in the image, we basically give the video type input program, and it blackens all colors not defined as skin color.


how to start:
1. Turn on the camera
2. Use of imutils image processing functions for resizing
3. Define the lower and upper boundaries for pixel intensities to be considered skin(boundaries are for the HSV color space)
4. Use this kernel to perform two iterations of erosions and dilations, respectively to remove the small false-positive skin regions in the image
5. Smooth the mask slightly using a Gaussian blur
6. At the end display the results side-by-side view of the original frame along with the frame with skin detected in it
