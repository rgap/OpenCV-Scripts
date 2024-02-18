import cv2
import numpy as np

img = cv2.imread("moneda.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
t, dst = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", dst)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(dst, kernel, iterations=4)
cv2.imshow("erosion", erosion)
dilatacion = cv2.dilate(erosion, kernel, iterations=4)
cv2.imshow("dilatacion", dilatacion)
(contours, _) = cv2.findContours(dilatacion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

valor = 0.0
for c in contours:
    area = cv2.contourArea(c)
    print(area)
    if area > 5000:
        cv2.drawContours(img, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)
        if area < 11000:
            valor = valor + 0.1
        if area > 11000 and area < 13000:
            valor = valor + 0.2
        if area > 13000:
            valor = valor + 5.0

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(
    img,
    "Valor: " + str(round(valor, 2)),
    (586, 30),
    font,
    0.68,
    (0, 255, 0),
    2,
    cv2.LINE_AA,
)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
