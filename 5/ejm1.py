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
    dilated = cv2.dilate(eroded, kernel, iterations=4)
    cv2.imshow("dilated", dilated)

    (contours, _) = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2, cv2.LINE_AA)
    for c in contours:
        area = cv2.contourArea(c)

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(
        img, "Area: " + str(area), (722, 30), font, 0.65, (0, 0, 255), 1, cv2.LINE_AA
    )

    cv2.imshow("1", img)

    # res = cv2.bitwise_and(img, img, mask=dilated)
    # cv2.imshow("PDI41", res)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
