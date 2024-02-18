import cv2
import numpy as np

img = np.zeros((370, 711, 3), np.uint8)
img_circle = cv2.circle(img, (426, 205), 140, (255, 255, 255), -1)  # -1 sin contorno

img_ball = cv2.imread("ball.png")

result = cv2.bitwise_and(img, img_ball)
cv2.imshow("img_circle", img_circle)
cv2.imshow("img_ball", img_ball)
cv2.imshow("resultado", result)

print("img_circle shape", img_circle.shape[:2])
print("img_ball shape", img_ball.shape[:2])

cv2.waitKey(0)
cv2.destroyAllWindows()
