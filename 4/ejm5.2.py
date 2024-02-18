import cv2
import numpy as np

img = cv2.imread("pelota.jpg", 0)  # 0 para escala de grises
kernel = np.ones((5, 5), np.uint8)

# Dilate
dilated = cv2.dilate(img, kernel, iterations=1)

# Erosion
eroded = cv2.erode(dilated, kernel, iterations=1)


cv2.imshow("img", img)
cv2.imshow("1_dilated", dilated)
cv2.imshow("2_eroded", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
