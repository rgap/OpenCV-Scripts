import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

x = eval(input("Ingrese X: "))
y = eval(input("Ingrese Y: "))
x1 = eval(input("Ingrese X1: "))
y1 = eval(input("Ingrese Y1: "))

cv2.line(image, (x, y), (x1, y1), (255, 255, 255), 1)

cv2.putText(
    image,
    f"(x:{x}, y:{y})",
    (x, y),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (255, 255, 255),
    1,
)
cv2.putText(
    image,
    f"(x1:{x1}, y1:{y1})",
    (x1, y1),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (255, 255, 255),
    1,
)

cv2.imshow("imagen", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
