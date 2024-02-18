import cv2

img1 = cv2.imread("3.png")
img2 = cv2.imread("4.png")

img3 = cv2.add(img1, img2)

cv2.imshow("resultado", img3)

print(img1[0, 0])
print(img2[0, 0])
print(img3[0, 0])

cv2.waitKey(0)
cv2.destroyAllWindows()
