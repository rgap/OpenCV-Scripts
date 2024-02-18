import cv2  # libreria de procesamiento de imagen
import numpy as np  # libreria para matrices

img = cv2.imread("frutas.jpg")
font = cv2.FONT_HERSHEY_COMPLEX  # tipo de letra
# texto
cv2.putText(
    img, "Manaza Verde", (490, 163), font, 0.68, (255, 0, 0), 1, cv2.LINE_AA
)  # dibujar texto
# texto (imagen, texto, posicion, tipo de letra, tamaño, color (B, G, R), grosor, modelo)

# region
cv2.rectangle(img, (490, 168), (700, 415), (255, 0, 0), 3)

cv2.imshow("1", img)

cv2.waitKey(0)  # wait for a keyboard input
cv2.destroyAllWindows()
