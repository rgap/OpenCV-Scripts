import cv2

cap = cv2.VideoCapture("aeropuerto.mp4")  # toda camara disponible
frame_number = 1

while True:
    ret, frame = cap.read()  # ler info de camara
    # ret es el audio
    cv2.imshow("video", frame)  # mostrar camara

    k = cv2.waitKey(1)  # esperar un 1 seg
    if k == 27:  # techa esc
        break
    if k == ord("s"):  # techa esc
        cv2.imwrite(
            f"frame_{frame_number}.jpg", frame
        )  # Save the frame with the frame number.
        frame_number += 1

cap.release()  # apagar camara
cv2.destroyAllWindows()
