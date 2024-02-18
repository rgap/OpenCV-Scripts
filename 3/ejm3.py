import cv2
import numpy as np

img = cv2.imread("img.jpg", 0)
res = cv2.GaussianBlur(img, (25, 25), 0)

th, ret = cv2.threshold(res, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("umbral", img)
cv2.imshow("resultado", ret)
print(th)

cv2.waitKey(0)
cv2.destroyAllWindows()
