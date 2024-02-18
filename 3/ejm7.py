import cv2
import numpy as np


def nothing(x):
    pass


# Start video capture
cap = cv2.VideoCapture(0)

# Create a window for the trackbars
cv2.namedWindow("Trackbars")

# Create trackbars for lower HSV
cv2.createTrackbar("Lower H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("Lower S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Lower V", "Trackbars", 0, 255, nothing)

# Create trackbars for upper HSV
cv2.createTrackbar("Upper H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("Upper S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Upper V", "Trackbars", 255, 255, nothing)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get current positions of the trackbars
    lower_h = cv2.getTrackbarPos("Lower H", "Trackbars")
    lower_s = cv2.getTrackbarPos("Lower S", "Trackbars")
    lower_v = cv2.getTrackbarPos("Lower V", "Trackbars")
    upper_h = cv2.getTrackbarPos("Upper H", "Trackbars")
    upper_s = cv2.getTrackbarPos("Upper S", "Trackbars")
    upper_v = cv2.getTrackbarPos("Upper V", "Trackbars")

    # Define the HSV range based on trackbar positions
    lower = np.array([lower_h, lower_s, lower_v])
    upper = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("resultado", res)

    if cv2.waitKey(1) & 0xFF == 27:  # Exit with ESC key
        break

cap.release()
cv2.destroyAllWindows()
