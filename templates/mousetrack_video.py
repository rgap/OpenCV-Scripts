import cv2


# Callback function to capture mouse events
def mouse_position(event, mouseX, mouseY, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        param["mouse_pos"] = (mouseX, mouseY)


def display_mouse_position_on_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera could not be opened.")
        return
    mouse_info = {"mouse_pos": (0, 0)}
    cv2.namedWindow("Camera Feed")
    cv2.setMouseCallback("Camera Feed", mouse_position, mouse_info)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        mouse_x, mouse_y = mouse_info["mouse_pos"]

        cv2.putText(
            frame,
            f"Mouse Position: ({mouse_x}, {mouse_y})",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
        )

        # Texto
        cv2.putText(
            frame,
            f"(x:{868}, y:{100})",
            (868, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1,
        )

        # Linea
        cv2.line(frame, (868, 100), (349, 721), (255, 255, 255), 1)

        cv2.imshow("Camera Feed", frame)

        # Check if 'm' is pressed
        if cv2.waitKey(1) & 0xFF == ord("m"):
            print(f"Mouse Position: ({mouse_x}, {mouse_y})")

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    display_mouse_position_on_camera()
