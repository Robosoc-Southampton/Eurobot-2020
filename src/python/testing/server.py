import socket
import cv2, pickle

server_socket = socket.socket()
server_socket.bind(('192.168.12.1', 8000))
server_socket.listen(0)

c = server_socket.accept()[0]
try:
    while True:
        imgsize_data = c.recv(32)
        if imgsize_data:
            jpg_data = b''
            imgsize = int(imgsize_data.decode('ascii'))

            # ack
            c.send(b'\x01')
            while True:
                jpg_chunk = c.recv(4096)
                jpg_data += jpg_chunk
                if len(jpg_data) >= imgsize:
                    img_data = pickle.loads(jpg_data)
                    img = cv2.imdecode(img_data, cv2.IMREAD_COLOR)

                    cv2.imshow('o', img)
                    cv2.waitKey(2)

                    # ack
                    c.send(b'\x01')
                    break
finally:
    server_socket.close()
