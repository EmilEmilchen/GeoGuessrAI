import socket
from PIL import Image
import io
import geo

def handle_client(client_socket):
    # Empfange die Bildgröße
    size = int.from_bytes(client_socket.recv(4), 'big')
    
    # Empfange das Bild
    image_data = b''
    while len(image_data) < size:
        packet = client_socket.recv(4096)
        if not packet:
            break
        image_data += packet
    
    # Lade das Bild
    image = Image.open(io.BytesIO(image_data))
    
    # Verarbeite das Bild
    result = geo.identify(image, 5)
    
    # Sende die Ergebnisse zurück
    client_socket.sendall(result.encode('utf-8'))
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("Server läuft...")

    while True:
        client_socket, addr = server.accept()
        print(f"Verbindung von {addr} akzeptiert")
        handle_client(client_socket)

if __name__ == "__main__":
    main()