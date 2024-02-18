import cv2  # libreria de procesamiento de imgs

img = cv2.imread("/Users/rgap/Desktop/vision/imagen.jpg")
cv2.imshow("prueba1", img)

cv2.waitKey(0)  # wait for a keyboard input
cv2.destroyAllWindows()
