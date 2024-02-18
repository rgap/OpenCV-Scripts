import cv2

cap = cv2.VideoCapture(0)  # toda camara disponible

while True:
    ret, frame = cap.read()  # ler info de camara
    # ret es el audio

    cv2.imshow("frame", frame)
    cols, rows = frame.shape[:2]
    print("original", rows, cols)

    res = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("res", res)
    cols, rows = res.shape[:2]
    print("resized", rows, cols)

    k = cv2.waitKey(1)  # esperar un 1 seg
    if k == 27:  # techa esc
        break

cap.release()  # apagar camara
cv2.destroyAllWindows()
