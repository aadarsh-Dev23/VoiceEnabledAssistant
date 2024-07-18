import cv2
import os

def capture_and_save_image():
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    if ret:
        # Save the captured frame as an image file
        img_name = "captured_image.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Image saved as {img_name}")
    else:
        print("Error: Failed to capture image.")

if __name__ == "__main__":
    capture_and_save_image()
