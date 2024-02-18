import cv2
import numpy as np


# Callback function to capture mouse events
def mouse_position(event, mouse_x, mouse_y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        # Update the mouse position
        param["mouse_pos"] = (mouse_x, mouse_y)


def display_mouse_position():
    # image = np.zeros((512, 512, 3), np.uint8)
    image = cv2.imread("ball.png")
    cv2.namedWindow("Mouse Position Display")

    mouse_info = {"mouse_pos": (0, 0)}
    cv2.setMouseCallback("Mouse Position Display", mouse_position, mouse_info)

    while True:
        display_image = image.copy()

        mouse_x, mouse_y = mouse_info["mouse_pos"]
        cv2.putText(
            display_image,
            f"Mouse Position: ({mouse_x}, {mouse_y})",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
        )

        # Texto
        cv2.putText(
            display_image,
            f"(x:{93}, y:{277})",
            (93, 277),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1,
        )

        # Linea
        cv2.line(display_image, (93, 277), (453, 124), (255, 255, 255), 1)

        if cv2.waitKey(1) & 0xFF == ord("m"):
            print(f"Mouse Position: ({mouse_x}, {mouse_y})")

        cv2.imshow("Mouse Position Display", display_image)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    display_mouse_position()
