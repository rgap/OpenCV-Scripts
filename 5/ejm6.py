import cv2
import numpy as np

cap = cv2.VideoCapture("aeropuerto.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()
color = (0, 0, 255)
while True:
    ret, frame = cap.read()
    if ret == False:
        break
    frame = cv2.resize(frame, None, fx=0.5, fy=0.4, interpolation=cv2.INTER_CUBIC)

    area_pts = np.array(
        [[340, 320], [600, 320], [850, frame.shape[0]], [140, frame.shape[0]]]
    )
    frame = cv2.drawContours(frame, [area_pts], -1, color, 3)
    color = (0, 255, 0)

    imAux = np.zeros(shape=frame.shape[:2], dtype=np.uint8)
    imAux = cv2.drawContours(imAux, [area_pts], -1, (255, 255, 255), -1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imAux = cv2.bitwise_and(gray, gray, mask=imAux)
    imAux = fgbg.apply(imAux)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(imAux, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=2)

    # Find contours
    cnts, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 500:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("imAux", imAux)
    cv2.imshow("dilation", dilation)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
