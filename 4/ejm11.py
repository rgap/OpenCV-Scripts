import cv2
import numpy as np


def nothing(x):
    pass


cv2.createTrackbar("Hmin", "PDI41", 0, 255, nothing)
cv2.createTrackbar("Hmax", "PDI41", 0, 255, nothing)
cv2.createTrackbar("Smin", "PDI41", 0, 255, nothing)
cv2.createTrackbar("Smax", "PDI41", 0, 255, nothing)
cv2.createTrackbar("Vmin", "PDI41", 0, 255, nothing)
cv2.createTrackbar("Vmax", "PDI41", 0, 255, nothing)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos("Hmin", "PDI41")
    hmax = cv2.getTrackbarPos("Hmax", "PDI41")
    smin = cv2.getTrackbarPos("Smin", "PDI41")
    smax = cv2.getTrackbarPos("Smax", "PDI41")
    vmin = cv2.getTrackbarPos("Vmin", "PDI41")
    vmax = cv2.getTrackbarPos("Vmax", "PDI41")

    lower = np.array([hmin, smin, vmin])
    upper = np.array([hmax, smax, vmax])

    lower = np.array([17, 174, 146])
    upper = np.array([24, 233, 209])

    mask = cv2.inRange(hsv, lower, upper)
    cv2.imshow("mask", mask)

    # kernel = np.ones((7, 7), np.uint8)
    # # Erosion
    # eroded = cv2.erode(mask, kernel, iterations=3)
    # # Dilate
    # dilated = cv2.dilate(eroded, kernel, iterations=5)
    # cv2.imshow("dilated", dilated)

    x, y, w, h = cv2.boundingRect(mask)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("processed", frame)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("object", res)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
