import cv2
import numpy as np

img = cv2.imread("frutas.jpg")
cv2.line(img, (490, 200), (684, 200), (0, 100, 200), 6)
cv2.line(img, (684, 200), (684, 394), (0, 100, 200), 6)
cv2.line(img, (684, 394), (490, 394), (0, 100, 200), 6)
cv2.line(img, (490, 394), (490, 200), (0, 100, 200), 6)


cv2.imshow("1", img)

cv2.waitKey(0)  # wait for a keyboard input
cv2.destroyAllWindows()
