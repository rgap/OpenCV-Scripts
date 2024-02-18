import cv2
import numpy as np

img = cv2.imread("frutas.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_roja = np.array([113, 0, 50])
upper_roja = np.array([179, 255, 255])

mask = cv2.inRange(hsv, lower_roja, upper_roja)

bola = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("img", img)
cv2.imshow("mask", mask)
cv2.imshow("resultado", bola)

cv2.waitKey(0)
cv2.destroyAllWindows()
