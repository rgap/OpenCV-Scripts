import cv2
import numpy as np

img = np.zeros((370, 711, 3), np.uint8)
# img = cv2.imread("ball.png")

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
