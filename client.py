import socket
import time
import keyboard
from PIL import ImageGrab
import io

def main():
    print("Press Shift + I to capture a screenshot and identify the image.")
    while True:
        if keyboard.is_pressed("shift") and keyboard.is_pressed("i"):
            print("Capturing...")

            # Capture the screen.
            screenshot = ImageGrab.grab(bbox=(114, 89, 1335, 957))

            print("captured")
            print("Sending to server...")

            # Verbinde mit dem Server
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('SERVER_IP', 9999))  # Ersetzen Sie 'SERVER_IP' durch die IP-Adresse des Servers

            # Konvertiere das Bild in Bytes
            img_byte_arr = io.BytesIO()
            screenshot.save(img_byte_arr, format='PNG')
            img_bytes = img_byte_arr.getvalue()

            # Sende die Bildgröße
            client.send(len(img_bytes).to_bytes(4, 'big'))

            # Sende das Bild
            client.sendall(img_bytes)

            # Empfange die Ergebnisse
            result = client.recv(4096).decode('utf-8')
            print("Result:", result)

            # Add a delay to prevent continuous captures on a single keypress.
            time.sleep(1)

if __name__ == "__main__":
    main()