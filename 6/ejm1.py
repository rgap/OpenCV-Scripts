import cv2

cascada_rostro = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

img = cv2.imread("faces.jpg")
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
coordenadas_rostros = cascada_rostro.detectMultiScale(img_gris, 1.3, 5)
for x, y, ancho, alto in coordenadas_rostros:
    cv2.rectangle(img, (x, y), (x + ancho, y + alto), (0, 0, 255), 3)

cv2.imshow("Output", img)
print("InMostrando resultado. Pulsa cualquier tecla para salir. \n")

cv2.waitKey(0)
cv2.destroyAllWindows()
