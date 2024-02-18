import cv2
import numpy as np

gray = cv2.imread("herramientas.jpg", cv2.IMREAD_GRAYSCALE)
t, dst = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)  # UMBRALIZACION BINARIA
t1, dst1 = cv2.threshold(
    gray, 170, 255, cv2.THRESH_BINARY_INV
)  # UMBRALIZACION BINARIA INVERSA
t2, dst2 = cv2.threshold(gray, 170, 255, cv2.THRESH_TRUNC)  # UMBRALIZACION TRUNCADA
t3, dst3 = cv2.threshold(gray, 170, 255, cv2.THRESH_TOZERO)  # UMBRALIZACION A CERO
t4, dst4 = cv2.threshold(
    gray, 170, 255, cv2.THRESH_TOZERO_INV
)  # UMBRALIZACION A CERO INVERSA

cv2.imshow("GRIS", gray)
cv2.imshow("UMBRALIZACION BINARIA", dst)
cv2.imshow("UMBRALIZACION BINARIA INVERSA", dst1)
cv2.imshow("UMBRALIZACION TRUNCADA", dst2)
cv2.imshow("UMBRALIZACION A CERO", dst3)
cv2.imshow("UMBRALIZACION A CERO INVERSA", dst4)

cv2.waitKey(0)
cv2.destroyAllWindows()
