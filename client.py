import socket
import time
import pyscreenshot as ImageGrab
import io
import tkinter as tk
from tkinter import messagebox

def capture_and_send_screenshot():
    print("Capturing...")

    try:
        # Capture the screen.
        screenshot = ImageGrab.grab(bbox=(0, 175, 1570, 1070))  # X1,Y1,X2,Y2
    except Exception as e:
        print(f"Screenshot failed: {e}")
        messagebox.showerror("Error", f"Screenshot failed: {e}")
        return

    print("captured")
    print("Sending to server...")

    try:
        # Verbinde mit dem Server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.105.165', 9999))  # Ersetzen Sie 'SERVER_IP' durch die IP-Adresse des Servers

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
        messagebox.showinfo("Result", f"Result: {result}")
    except Exception as e:
        print(f"Failed to send/receive data: {e}")
        messagebox.showerror("Error", f"Failed to send/receive data: {e}")
    finally:
        client.close()

def main():
    root = tk.Tk()
    root.title("Screenshot Client")

    capture_button = tk.Button(root, text="Capture Screenshot", command=capture_and_send_screenshot)
    capture_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()