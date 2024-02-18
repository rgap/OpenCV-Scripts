import os

import cv2

# Folder for captured images
image_folder = "n"
if not os.path.exists(image_folder):
    print("Creating folder: ", image_folder)
    os.makedirs(image_folder)

# Start video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Camera could not be accessed.")
    exit()

# Rectangle coordinates
x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Copy of the frame
    imAux = frame.copy()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # ROI extraction and resizing
    objeto = imAux[y1:y2, x1:x2]
    objeto = cv2.resize(objeto, (38, int(objeto.shape[0] * (38 / objeto.shape[1]))))

    k = cv2.waitKey(1)
    if k == ord("s"):
        img_name = os.path.join(image_folder, f"objeto_{count}.jpg")
        cv2.imwrite(img_name, objeto)
        print(f"Image stored: {img_name}")
        count += 1
    elif k == 27:
        print("Escape hit, closing...")
        break

    cv2.imshow("frame", frame)
    cv2.imshow("objeto", objeto)

cap.release()
cv2.destroyAllWindows()
