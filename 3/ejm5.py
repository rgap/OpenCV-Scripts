import cv2
import numpy as np

img = cv2.imread("frutas.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_verde = np.array([34, 69, 175])
upper_verde = np.array([44, 255, 240])

mask = cv2.inRange(hsv, lower_verde, upper_verde)

bola = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("img", img)
cv2.imshow("mask", mask)
cv2.imshow("resultado", bola)

cv2.waitKey(0)
cv2.destroyAllWindows()
