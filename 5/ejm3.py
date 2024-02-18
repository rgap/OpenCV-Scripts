import cv2
import numpy as np


def nothing(x):
    pass


# Initialize the GUI window for sliders
cv2.namedWindow("Settings")

# Create trackbars with initial values
cv2.createTrackbar("Threshold", "Settings", 146, 255, nothing)
cv2.createTrackbar(
    "Kernel Size", "Settings", 5, 20, nothing
)  # Max kernel size 20 for more flexibility
cv2.createTrackbar("Erosion Iter", "Settings", 9, 10, nothing)
cv2.createTrackbar("Dilation Iter", "Settings", 9, 10, nothing)

img_original = cv2.imread("moneda.jpg")

while True:
    img = img_original.copy()  # Work on a copy of the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Get current positions of the trackbars
    thresh = cv2.getTrackbarPos("Threshold", "Settings")
    kernel_size = cv2.getTrackbarPos("Kernel Size", "Settings")
    erosion_iter = cv2.getTrackbarPos("Erosion Iter", "Settings")
    dilation_iter = cv2.getTrackbarPos("Dilation Iter", "Settings")

    # Apply threshold
    _, dst = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)

    # Create a kernel based on trackbar position
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Apply erosion and dilation
    erosion = cv2.erode(dst, kernel, iterations=erosion_iter)
    dilation = cv2.dilate(erosion, kernel, iterations=dilation_iter)

    # Find contours
    contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    valor = 0.0
    for c in contours:
        area = cv2.contourArea(c)
        print(area)
        if area > 5000:
            cv2.drawContours(img, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)
            if area < 10500:
                valor += 0.1
            elif area < 12000:
                valor += 0.2
            else:
                valor += 5.0
    print("/n/n")

    # Display the total value on the image
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(
        img,
        f"Valor: {round(valor, 2)}",
        (586, 30),
        font,
        0.68,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )

    # Show images
    cv2.imshow("binary", dst)
    cv2.imshow("erosion", erosion)
    cv2.imshow("dilation", dilation)
    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cv2.destroyAllWindows()
