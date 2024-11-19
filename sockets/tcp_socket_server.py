from http import server
import socket

SERVER_PORT = 12001
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost',SERVER_PORT))
server_socket.listen(1)
print("socket ready to receive")
while True:
    connection_socket, addr = server_socket.accept()
    sentence = connection_socket.recv(1024).decode()
    modified_message = sentence.upper() + " HELLO"
    print(f"received {modified_message}")
    connection_socket.send(modified_message.encode())
    connection_socket.close()