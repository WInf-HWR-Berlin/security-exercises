from http import server
import socket

SERVER_PORT = 12000
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('',SERVER_PORT))
print("socket ready to receive")
while True:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.decode().upper() + " HELLO"
    print(f"received {modified_message}")
    server_socket.sendto(modified_message.encode(), client_address)