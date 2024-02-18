import cv2
import numpy as np

img_fruta = cv2.imread("frutas.jpg")
cv2.imshow("img_fruta", img_fruta)
cols, rows = img_fruta.shape[:2]
print(rows, cols)

res = cv2.resize(img_fruta, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow("res", res)
cols, rows = res.shape[:2]
print(rows, cols)

cv2.waitKey(0)
cv2.destroyAllWindows()
