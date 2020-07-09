# Tamir Atia

import numpy as np
import cv2
from pyimagesearch import imutils

# define the upper and lower boundaries of the HSV pixel that considered skin
LowerB = np.array([0, 48, 80], dtype="uint8")
UpperB = np.array([20, 255, 255], dtype="uint8")

camera = cv2.VideoCapture(0)

# keep looping over the Images in the video

while True:
    # grab the current image
    (grabbed, Image) = camera.read()

    # Resize to window video
    # and converting the picture from BGR to HSV
    # with applying the boundaries of the HSV pixel (defining skin color)
    Image = imutils.resize(Image, width=400)
    converted = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(converted, LowerB, UpperB)

    # using an elliptical kernel
    # and applying erosions and dilations to the mask
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))
    skinMask = cv2.erode(skinMask, kernel, iterations=2)
    skinMask = cv2.dilate(skinMask, kernel, iterations=2)

    # smooth the mask slightly using a Gaussian blur
    # and applying the skin mask to our frame
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    SkinD = cv2.bitwise_and(Image, Image, mask=skinMask)

    # show the skin in the picture along with the mask
    cv2.imshow("Skin Detect", np.hstack([Image, SkinD]))
    #  pressing the button "q" to brake the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
