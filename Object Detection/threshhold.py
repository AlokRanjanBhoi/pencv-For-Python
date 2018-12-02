import cv2
import numpy as np
bw = cv2.imread("world_map.jpg", 0)
height, width = bw.shape[0:2]
cv2.imshow("Original BW", bw)

binary = np.zeros([height,width,1], 'uint8')

thresh = 85

for row in range(0,height):
    for col in range(0,width):
        if bw[row] [col]>thresh:
            binary[row] [col]=255

cv2.imshow("Show Binary", binary)
ret, thresh = cv2.threshold(bw,thresh,255,cv2.THRESH_BINARY)

cv2.waitKey(0)
cv2.destoryAllWindows()
