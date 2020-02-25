import socket
import cv2, pickle
from vision.camera import VisionCamera

client_socket = socket.socket()
client_socket.connect(('192.168.12.1', 8000))

try:
    with VisionCamera((640, 480), 60) as camera:
        for img in camera.videoStream():
            _, data = cv2.imencode('.jpg', img)
            b = pickle.dumps(data)
            client_socket.sendall(str(len(b)).encode('ascii'))

            # wait for ack
            r = client_socket.recv(1)
            while r != b'\x01':
                r = client_socket.recv(1)

            client_socket.sendall(b)

            # wait for ack
            r = client_socket.recv(1)
            while r != b'\x01':
                r = client_socket.recv(1)
finally:
    client_socket.close()
