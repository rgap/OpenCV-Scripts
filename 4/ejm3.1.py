import cv2
import numpy as np

img = cv2.imread("pelota.jpg", 0)  # 0 para escala de grises
kernel = np.ones((5, 5), np.uint8)

# Erosion
eroded = cv2.erode(img, kernel, iterations=4)
cv2.imshow("1", img)
cv2.imshow("2", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
