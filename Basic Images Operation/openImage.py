import numpy as np
import cv2

img = cv2.imread("Alok.jpg")
#cv2.namedWindow("Images", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.imwrite("outputImg.jpg",img)
