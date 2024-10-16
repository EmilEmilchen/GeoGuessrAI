import socket
import pyscreenshot as ImageGrab
import io
import tkinter as tk
from tkinter import messagebox
import json

def capture_and_send_screenshot():
    print("Capturing...")

    try:
        # Capture the screen.
        screenshot = ImageGrab.grab(bbox=(200, 300, 3200, 2200))  # X1,Y1,X2,Y2
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
sss
        # Empfange die Ergebnisse
        result_json = client.recv(4096).decode('utf-8')
        result = json.loads(result_json)
        print("Result:", result)
        display_result(result)
    except Exception as e:
        print(f"Failed to send/receive data: {e}")
        messagebox.showerror("Error", f"Failed to send/receive data: {e}")
    finally:
        client.close()

def display_result(result):
    countries, percentages = result
    result_str = "\n".join([f"{country}: {percent:.2f}%" for country, percent in zip(countries, percentages)])
    result_window = tk.Toplevel()
    result_window.title("Result")

    result_text = tk.Text(result_window, wrap='word')
    result_text.insert(tk.END, result_str)
    result_text.config(state=tk.DISABLED)
    result_text.pack(padx=10, pady=10)

    close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
    close_button.pack(pady=10)

def main():
    root = tk.Tk()
    root.title("Screenshot Client")

    capture_button = tk.Button(root, text="Capture Screenshot", command=capture_and_send_screenshot)
    capture_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()