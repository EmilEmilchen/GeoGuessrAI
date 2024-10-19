import cv2

def main():
    # Öffne die Webcam (Standard-Webcam hat den Index 0)
    cap = cv2.VideoCapture(4)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to quit.")

    while True:
        # Erfasse einen Frame von der Webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image.")
            break

        # Zeige den Frame in einem Fenster an
        cv2.imshow('Webcam Check', frame)

        # Beenden, wenn 'q' gedrückt wird
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()