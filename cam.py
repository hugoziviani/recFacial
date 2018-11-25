import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while 1:
	img = cap.read()
	cv.imshow("img",img)
	k = cv.waitKey(30)
	if k == 27:
		break

cap.release()

