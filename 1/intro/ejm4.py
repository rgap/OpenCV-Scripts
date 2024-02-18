import cv2

cap = cv2.VideoCapture("aeropuerto.mp4")  # toda camara disponible

while True:
    ret, frame = cap.read()  # ler info de camara
    # ret es el audio
    cv2.imshow("video", frame)  # mostrar camara

    k = cv2.waitKey(1)  # esperar un 1 seg
    if k == 27:  # techa esc
        break

cap.release()  # apagar camara
cv2.destroyAllWindows()
