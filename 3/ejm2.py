import cv2
import numpy as np

img = cv2.imread("img.jpg", 0)
res = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
res1 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

cv2.imshow("umbral", img)
cv2.imshow("resultado", res)
cv2.imshow("resultado1", res1)

cv2.waitKey(0)
cv2.destroyAllWindows()
