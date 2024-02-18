import cv2
import numpy as np

img = cv2.imread("frutas.jpg")


def nothing(x):
    pass


cv2.namedWindow("PDI41")
cv2.createTrackbar("Hmin", "PDI41", 0, 255, nothing)
cv2.createTrackbar("Hmax", "PDI41", 0, 255, nothing)
cv2.createTrackbar("Smin", "PDI41", 0, 255, nothing)
cv2.createTrackbar("Smax", "PDI41", 0, 255, nothing)
cv2.createTrackbar("Vmin", "PDI41", 0, 255, nothing)
cv2.createTrackbar("Vmax", "PDI41", 0, 255, nothing)

while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos("Hmin", "PDI41")
    hmax = cv2.getTrackbarPos("Hmax", "PDI41")
    smin = cv2.getTrackbarPos("Smin", "PDI41")
    smax = cv2.getTrackbarPos("Smax", "PDI41")
    vmin = cv2.getTrackbarPos("Vmin", "PDI41")
    vmax = cv2.getTrackbarPos("Vmax", "PDI41")

    lower = np.array([hmin, smin, vmin])
    upper = np.array([hmax, smax, vmax])

    lower = np.array([29, 59, 128])
    upper = np.array([45, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    cv2.imshow("mask", mask)

    kernel = np.ones((7, 7), np.uint8)
    # Erosion
    eroded = cv2.erode(mask, kernel, iterations=3)
    # Dilate
    dilated = cv2.dilate(eroded, kernel, iterations=5)
    cv2.imshow("dilated", dilated)

    x, y, w, h = cv2.boundingRect(dilated)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
    cv2.imshow("img", img)

    # res = cv2.bitwise_and(img, img, mask=dilated)
    # cv2.imshow("PDI41", res)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
