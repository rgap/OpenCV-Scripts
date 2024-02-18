import cv2

# Load the Haar Cascade for frontal face detection
cascada_rostro = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_alt.xml"
)

# Initialize the video capture object to read from the default camera
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #  Smaller values, like 1.01, would make the detection more thorough but slower, as the algorithm would need to process more scales.
    # Detect faces in the grayscale frame
    coordenadas_rostros = cascada_rostro.detectMultiScale(img_gris, 1.1, 5)

    for x, y, ancho, alto in coordenadas_rostros:
        # Draw a rectangle around the face
        cv2.rectangle(img, (x, y), (x + ancho, y + alto), (0, 0, 255), 3)
        # Define the region of interest in the grayscale and color frames (the face)
        roi_gris = img_gris[y : y + alto, x : x + ancho]
        roi_color = img[y : y + alto, x : x + ancho]

    # Display the resulting frame
    cv2.imshow("Camera Output", img)
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
