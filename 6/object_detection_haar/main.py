import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

majinBooClassif = cv2.CascadeClassifier("classifier/cascade.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        continue  # Skip the rest of the loop if no frame is captured

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    object = majinBooClassif.detectMultiScale(
        gray, scaleFactor=5, minNeighbors=91, minSize=(70, 78)
    )

    for x, y, w, h in object:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "objeto", (x, y - 10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Correctly wait for ESC key
        break

cap.release()
cv2.destroyAllWindows()
