import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(
    img, (0, 0), (200, 512), (0, 0, 255), 8
)  # inicio, final, color (B, G, R), grosor

cv2.imshow("1", img)

cv2.waitKey(0)  # wait for a keyboard input
cv2.destroyAllWindows()
